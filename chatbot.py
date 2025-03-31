import time

def ask_questions():
    """Ask user travel-related questions and collect responses."""
    user_data = {}

    print("\nWelcome to the AI Travel Planner! Let's plan your trip 🚀")

    user_data["destination"] = input("✈️ Where do you want to go? ")
    user_data["start_location"] = input("📍 Where are you traveling from? ")
    user_data["budget"] = input("💰 What is your budget (low, medium, high)? ")
    user_data["trip_duration"] = input("📅 How many days will you stay? ")
    user_data["purpose"] = input("🎯 What’s the purpose of your trip (vacation, business, adventure, etc.)? ")
    user_data["preferences"] = input("🏞️ What activities do you prefer (nature, history, shopping, nightlife, etc.)? ")

    print("\n✅ Collecting details... Please wait!")
    time.sleep(2)

    return user_data

if __name__ == "__main__":
    user_info = ask_questions()
    print("\n🎉 Travel Plan Inputs Received! Here’s what we collected:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")
