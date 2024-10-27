🌦️ MyWeatherBot
MyWeatherBot is a Django-based web app integrated with a Telegram bot to provide real-time weather information by country. Users can retrieve weather updates directly from the bot or through the Django API.

🚀 Features
Weather Data Retrieval: Real-time weather information for any specified country.
RESTful API: Django API serves weather data in JSON format.
Telegram Bot: Users can get weather data via simple commands in Telegram.
📁 Project Structure
bash
Copy code
MyWeatherBot/
├── views.py           # Django view to handle API requests
├── mybot.py           # Telegram bot script
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
🛠️ Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/mhergoorgenian/MyWeatherBot.git
cd MyWeatherBot
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Set API Keys
Weather API Key: Replace API_KEY in views.py with your WeatherAPI key.
Telegram Bot Token: Replace TOKEN in mybot.py with your Telegram Bot token.
4. Run the Django Server
bash
Copy code
python manage.py runserver
5. Start the Telegram Bot
bash
Copy code
python mybot.py
💬 Usage
Telegram Bot Commands
/country [country_name]: Retrieve current weather for the specified country.
Example:
plaintext
Copy code
/country Japan
Django API Endpoint
The API endpoint provides weather data in JSON format.

Endpoint: http://127.0.0.1:8000/api/[country]
Example:
plaintext
Copy code
http://127.0.0.1:8000/api/Japan
❓ Troubleshooting
Make sure API keys are correctly set in views.py and mybot.py.
Confirm that the Django server is running before using the bot.
