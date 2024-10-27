import telebot
import requests
import os


TOKEN = 'bot token' 
bot = telebot.TeleBot(TOKEN)


DJANGO_API_URL = "your.ip/api/"  

def get_updates(offset=0):
    response = requests.get(f"{API_URL}/getUpdates", params={"offset": offset, "timeout": 100})
    result = response.json()
    messages = []

    for update in result.get("result", []):
        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text")
            if text and text.startswith("/country"):
                country = text.split(" ", 1)[1] if len(text.split(" ")) > 1 else None
                if country:
                    messages.append({"chat_id": chat_id, "country": country})
                else:
                    send_message(chat_id, "Please provide a country name. Usage: /country country_name")
            elif text and text.startswith("/start"):
                send_message(chat_id, "Welcome! Please provide a country name. Usage: /country country_name")
        offset = update["update_id"] + 1
    return messages, offset


def get_weather(country):
    try:
        response = requests.get(f"{DJANGO_API_URL}{country}/")
        response.raise_for_status()
        weather_data = response.json()

        weather_info = (
            f"Weather in {country.capitalize()}:\n"
            f"Temperature: {weather_data['current']['temp_c']}°C\n"
            f"Condition: {weather_data['current']['condition']['text']}\n"
            f"Humidity: {weather_data['current']['humidity']}%\n"
            f"Wind: {weather_data['current']['wind_kph']} km/h\n"
        )
        return weather_info

    except requests.RequestException:
        return "Error: Unable to retrieve data. Please try again later."


def send_message(chat_id, text):
    requests.post(f"{API_URL}/sendMessage", data={"chat_id": chat_id, "text": text})


last_update_id = 0
while True:
    messages, last_update_id = get_updates(last_update_id)
    for message in messages:
        chat_id = message["chat_id"]
        country = message["country"]
        weather_info = get_weather(country)
        send_message(chat_id, weather_info)
    time.sleep(1)

