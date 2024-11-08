from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.simple_message, name='simple_message'),
]