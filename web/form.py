from django import forms


class JoinForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8)
    next = forms.CharField(initial="/")
