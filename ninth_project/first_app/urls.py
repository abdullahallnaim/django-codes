from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_session ),
    path('get/',views.get_session ),
    path('del/',views.delete_session ),
]