from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.SignUp.as_view(), name='registration'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
]
