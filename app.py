import streamlit as st
import os
import requests

# Load API key (Use .env locally, secrets.toml on Streamlit)
HF_API_KEY = os.getenv("HF_API_KEY", st.secrets.get("HF_API_KEY"))

# Hugging Face API Configuration
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_huggingface(prompt):
    """Query the Hugging Face model and return a response."""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        response_data = response.json()
        if isinstance(response_data, list) and "generated_text" in response_data[0]:
            return response_data[0]['generated_text']
        return f"Error: Unexpected response format\nResponse: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}\nResponse: {response.text}"

def generate_itinerary(destination, duration, purpose, interests):
    """Generate a detailed travel itinerary based on user input."""
    prompt = (
        f"Create a travel itinerary for {destination} for {duration} days.\n"
        f"The purpose of the trip is {purpose} and the traveler is interested in {', '.join(interests)}.\n"
        f"Provide detailed recommendations on:\n"
        f"- Best places to visit\n"
        f"- Must-try food & local specialties\n"
        f"- Accommodation suggestions\n"
        f"- Cultural or adventure activities\n"
        f"Make it exciting and informative."
    )

    return query_huggingface(prompt)

# Streamlit UI
st.title("🌍 TRAVEL2DAY - Your AI-Powered Travel Planner 🚀")

destination = st.text_input("✈️ Where do you want to go?")
departure = st.text_input("📍 Where are you traveling from?")
budget = st.selectbox("💰 What is your budget?", ["Low", "Medium", "High"])
duration = st.number_input("📅 How many days will you stay?", min_value=1, max_value=30, value=5)
purpose = st.selectbox("🎯 What’s the purpose of your trip?", ["Vacation", "Business", "Adventure"])
interests = st.multiselect("🏞️ What activities do you prefer?", ["Nature", "History", "Shopping", "Nightlife"])

if st.button("Generate Itinerary"):
    if not HF_API_KEY:
        st.error("API Key is missing! Please set it in `.env` or Streamlit Secrets.")
    else:
        st.write("✅ Collecting details... Please wait!")
        itinerary = generate_itinerary(destination, duration, purpose, interests)
        st.subheader("📌 Your AI-Generated Travel Itinerary:")
        st.write(itinerary)
