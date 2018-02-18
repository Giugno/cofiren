from django.urls import path
from . import views

urlpatterns = [
    path('', views.presentation, name='presentation'),
    path('historique', views.historique, name='historique'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('liens', views.liens, name='liens'),
]
