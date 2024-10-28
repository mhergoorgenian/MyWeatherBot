import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from weather_bot import settings



BOT_TOKEN='botApi'
API_KEY = settings.API_KEY
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

class WebHookView(APIView):
    def get(self, request):
        webhook = request.GET.get('url')
        if webhook:
            response = requests.post(TELEGRAM_API_URL + "setWebhook?url=" + webhook).json()
            return Response(response)
        return Response({"error": "URL parameter not provided"}, status=400)



class SendMessageView(APIView):
    def handle_update(self, update):
        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text")
            if text and text.startswith("/country"):
                country = text.split(" ", 1)[1] if len(text.split(" ")) > 1 else None
                if country:
                    weather_response = self.get_data_view(country)
                    message_text = weather_response.data if isinstance(weather_response, Response) else 'Error retrieving weather data.'
                    self.send_message("sendMessage", {
                        'chat_id': chat_id,
                        'text': message_text
                    })

    def send_message(self, method, data):
        response = requests.post(TELEGRAM_API_URL + method, json=data)
        return response

    def post(self, request, format=None):
        update = json.loads(request.body.decode('utf-8'))
        self.handle_update(update)
        return Response('ok')

    def get_data_view(self, country):
        if not settings.API_KEY:
            return Response({"error": "API key not found"}, status=500)

        url = f"http://api.weatherapi.com/v1/current.json?key={settings.API_KEY}&q={country}&aqi=yes"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            weather_info = f"Weather in {country}:\n"
            weather_info += f"Temperature: {data['current']['temp_c']}°C\n"
            weather_info += f"Condition: {data['current']['condition']['text']}\n"
            weather_info += f"Wind: {data['current']['wind_kph']} kph\n"
            return Response(weather_info)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=500)
