# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp import views  # Assurez-vous d'importer la vue de votre application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', views.simple_message, name='simple_message'),
    path('', views.simple_message, name='home'),  # Ajoutez cette ligne pour l'URL vide (page d'accueil)
]
