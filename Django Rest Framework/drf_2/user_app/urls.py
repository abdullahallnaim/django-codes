from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
