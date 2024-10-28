
```markdown
# Weather Telegram Bot

This repository contains a simple Telegram bot that provides weather information based on user requests. The bot allows users to inquire about the weather in specific countries using the `/country` command.

## Features

- Responds to `/country <country_name>` command.
- Retrieves current weather data from the WeatherAPI.
- Sends weather information back to the user via Telegram.

## Technologies Used

- Python
- Django REST Framework
- Requests library for HTTP requests
- WeatherAPI for fetching weather data

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- A Telegram bot token (you can create one via [BotFather](https://core.telegram.org/bots#botfather))
- WeatherAPI key (sign up at [WeatherAPI](https://www.weatherapi.com/) to get an API key)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-telegram-bot.git
   cd weather-telegram-bot
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your API keys in `settings.py`:

   ```python
   BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   API_KEY = 'YOUR_WEATHER_API_KEY'
   ```

### Running the Bot

1. Start your Django development server:

   ```bash
   python manage.py runserver
   ```

2. Set the webhook for your Telegram bot to point to your server:

   You can use an external service like ngrok to expose your local server. Run ngrok and use the generated URL to set your webhook:

   ```bash
   ngrok http 8000
   ```

   Use the following command to set the webhook:

   ```bash
   curl -X POST "https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/setWebhook?url=https://<ngrok_subdomain>.ngrok.io/api/getpost/"
   ```

### Commands

- `/country <country_name>`: Retrieves and sends the current weather information for the specified country.

### Example

```plaintext
User: /country Germany
Bot: Weather in Germany:
     Temperature: 10°C
     Condition: Clear
     Wind: 5 kph
```


## Acknowledgements

- [Telegram Bot API](https://core.telegram.org/bots/api) for the bot functionality.
- [WeatherAPI](https://www.weatherapi.com/) for providing weather data.

```

### Notes:
- Make sure to replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_WEATHER_API_KEY` with the appropriate placeholders.
- Adjust the repository URL to your actual GitHub repository link.
- Add any additional sections or details as necessary, such as troubleshooting tips or further documentation on the code structure.
