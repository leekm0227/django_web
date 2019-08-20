from django.urls import path, include
from api import views

urlpatterns = [
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/', include('rest_auth.urls')),
    path('datas/<int:pk>/', views.Data.as_view()),
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('articles/<int:pk>/comments/', views.CommentList.as_view()),
    path('articles/<int:pk>/comments/<int:comment_id>/', views.CommentDetail.as_view()),
    path('logs/', views.Log.as_view()),
    path('tssr/', views.tssr)
]
