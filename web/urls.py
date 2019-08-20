from django.urls import path
from web import views


urlpatterns = [
    path('', views.Index.as_view()),
    path('join/', views.Join.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.logout),
    path('tssr/', views.Tssr.as_view()),
    path('article/', views.Article.as_view()),
    path('article/<int:pk>/', views.Article.as_view()),
]