from django.urls import path
from . import views

app_name = 'khiyaar'

urlpatterns = [
    path('', views.home),
]
