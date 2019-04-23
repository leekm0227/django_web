from django.shortcuts import render
import requests


def index(request):
    response = requests.get('http://127.0.0.1:8000/api/articles/')
    context = {} if response.status_code == 200 else context = {'list': response.json()}

    return render(request, 'index.html', context)
