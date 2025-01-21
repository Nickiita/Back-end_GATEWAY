from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://127.0.0.1:8001/main/register/", json=data)
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://127.0.0.1:8001/main/login/", json=data)
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://127.0.0.1:8001/main/logout/", json=data)
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://127.0.0.1:8001/main/users/", json=data)
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def read_user(request, user_id):
    if request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8001/main/users/{user_id}")
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_user(request, user_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        response = requests.put(f"http://127.0.0.1:8001/main/users/{user_id}/update/", json=data)
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        response = requests.delete(f"http://127.0.0.1:8001/main/users/{user_id}/delete/")
        return JsonResponse(response.json(), status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def handle_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://127.0.0.1:8001/main/review/", data=data)
        return HttpResponse(response.text, status=response.status_code)
    
    elif request.method == "GET":
        response = requests.get("http://127.0.0.1:8001/main/review/")
        return HttpResponse(response.text, status=response.status_code)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def review_success(request):
    response = requests.get("http://127.0.0.1:8001/main/review_success/")
    return HttpResponse(response.text, status=response.status_code)