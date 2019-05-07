from django.shortcuts import render
from django.conf import settings
from django.http import *
import requests

header = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}


def index(request):
    context = {}
    data = requests.get(settings.API_URL + 'articles/')

    if data.status_code == 200:
        context = {'list': data.json()}

    return render(request, 'index.html', context)


def login(request):
    if request.method == "POST":
        data = requests.post(settings.API_URL + 'auth/login/', data=request.body.decode('utf-8'), headers=header)

        if data.status_code == 200:
            data = data.json()
            response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            response.set_cookie(key="token", value=data["token"])
            return response
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()
