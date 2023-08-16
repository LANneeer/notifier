import requests
from rest_framework.response import Response
from rest_framework.views import APIView


class TelegramView(APIView):
    def get(self, request, *args, **kwargs):
        url = "https://api.example.com/data/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response({"error": "Failed to fetch data from external API"}, status=response.status_code)
