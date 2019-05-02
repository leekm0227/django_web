from django.shortcuts import render
from django.conf import settings
import requests


def index(request):
    response = requests.get(settings.API_URL + '/articles')
    context = {}

    if response.status_code == 200:
        context = {'list': response.json()}

    return render(request, 'index.html', context)
