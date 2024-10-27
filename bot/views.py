import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response




API_KEY = "apikey"

@api_view(['GET'])
def get_data_view(request, country):
    # Assuming `apikey` is stored in an environment variable
    
    
    if not API_KEY:
        return Response({"error": "API key not found"}, status=500)

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={country}&aqi=yes"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=response.status_code if response else 500)
    
    return Response(data)
