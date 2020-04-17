from django.urls import path

from . import views
app_name = 'social'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<str:username>/', views.user_profile, name='profile'),
]