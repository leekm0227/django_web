from django.urls import path, include
from api import views


urlpatterns = [
    path('auth/register', include('rest_auth.registration.urls')),
    path('auth/', include('rest_auth.urls')),
    path('articles', views.ArticleList.as_view()),
    path('articles/<int:pk>', views.ArticleDetail.as_view()),
]