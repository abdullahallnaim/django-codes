from django.urls import path
from . import views
urlpatterns = [
    path('contact/', views.contact),
    path('about/', views.about),
]