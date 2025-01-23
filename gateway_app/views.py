from django.http import JsonResponse
from django.conf import settings
import requests


def proxy_request(request):
    try:
        url = settings.URL_FIRST_SERVER
        response = requests.get(url)
        
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException as error:
        return JsonResponse({"error": str(error)}, status=500)