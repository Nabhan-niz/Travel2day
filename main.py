from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# Load API Key from .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_huggingface(prompt):
    """Query the Hugging Face model and return response."""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        response_data = response.json()
        return response_data[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}\nResponse: {response.text}"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/generate_itinerary", methods=["POST"])
def generate_itinerary():
    """Generate itinerary from user input."""
    data = request.json
    destination = data.get("destination")
    duration = data.get("duration")
    purpose = data.get("purpose")
    interests = data.get("interests")

    prompt = (
        f"Create a travel itinerary for {destination} for {duration} days.\n"
        f"The purpose of the trip is {purpose} and the traveler is interested in {interests}.\n"
        f"Provide detailed recommendations on:\n"
        f"- Best places to visit\n"
        f"- Must-try food & local specialties\n"
        f"- Accommodation suggestions\n"
        f"- Cultural or adventure activities\n"
        f"Make it exciting and informative."
    )

    itinerary = query_huggingface(prompt)
    return jsonify({"itinerary": itinerary})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
