from django.urls import path
from web import views


urlpatterns = [
    path('', views.index),
    path('login/', views.login),
]