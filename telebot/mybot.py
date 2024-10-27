import telebot
import requests
import os


TOKEN = 'bot token' 
bot = telebot.TeleBot(TOKEN)


DJANGO_API_URL = "your.ip/api/"  

@bot.message_handler(commands=['country'])
def get_country_weather(message):

    try:
        country = message.text.split()[1]
    except IndexError:
        bot.reply_to(message, "Please provide a country name. Usage: /country country_name")
        return


    try:
        response = requests.get(f"{DJANGO_API_URL}{country}/")
        response.raise_for_status()
        weather_data = response.json()


        weather_info = f"Weather in {country.capitalize()}:\n"
        weather_info += f"Temperature: {weather_data['current']['temp_c']}°C\n"
        weather_info += f"Condition: {weather_data['current']['condition']['text']}\n"
        weather_info += f"Humidity: {weather_data['current']['humidity']}%\n"
        weather_info += f"Wind: {weather_data['current']['wind_kph']} km/h\n"
        
        bot.reply_to(message, weather_info)

    except requests.RequestException:
        bot.reply_to(message, "Error: Unable to retrieve data. Please try again later.")

bot.polling()
