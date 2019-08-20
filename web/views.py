import json
from web.common import View
from django.shortcuts import render
from django.contrib import messages
from django.http import *
from .form import *


class Tssr(View):
    template = 'tesseract.html'


class Login(View):
    template = 'user/login.html'

    def post(self, req):
        form = LoginForm(req.POST)

        if form.is_valid():
            data = self.api(method='post', uri='auth/login/', data=form.cleaned_data)

            if data is not None:
                self.token = data["key"]
                data = self.api(uri='auth/user/')
                res = HttpResponseRedirect(req.POST["next"])
                res.set_cookie(key="token", value=self.enc(self.token))
                res.set_cookie(key="username", value=data['username'])
                return res

        messages.info(req, "plz check email, pwd")
        return render(req, self.template)

    def get(self, req, **kwargs):
        if self.token is not None:
            return HttpResponseRedirect("/")
        else:
            return super().get(req)


class Article(View):
    template = 'article.html'

    def get(self, req, **kwargs):
        if 'pk' in self.kwargs:
            print(self.kwargs['pk'])
            self.context['article'] = self.api(uri='articles/{pk}/'.format(pk=self.kwargs['pk']))
            self.context['comment'] = self.api(uri='articles/{pk}/comments/'.format(pk=self.kwargs['pk']))

        if 'article' in self.context:
            print(self.context['article'])

        if 'comment' in self.context:
            print(self.context['comment'])

        self.context['list'] = self.api(uri='articles/?page={page}'.format(page=req.GET.get('page', 1)))
        return super().get(req)


class Index(View):
    template = 'index.html'


class Join(View):
    template = 'user/join.html'

    def post(self, req):
        form = JoinForm(req.POST)

        if form.is_valid():
            data = self.api(method='post', uri='auth/register/', data=form.cleaned_data)

            if data is not None:
                self.token = data["key"]
                data = self.api(uri='auth/user/')
                res = HttpResponseRedirect('/')
                res.set_cookie(key="token", value=self.enc(self.token))
                res.set_cookie(key="username", value=data['username'])
                return res

        messages.error(req, "plz check email, name, pwd")
        return render(req, self.template)

    def get(self, req, **kwargs):
        if self.token is not None:
            return HttpResponseRedirect("/")
        else:
            return super().get(req)


def logout(req):
    res = HttpResponseRedirect(req.META['HTTP_REFERER'])
    res.delete_cookie(key="token")
    res.delete_cookie(key="username")
    return res
