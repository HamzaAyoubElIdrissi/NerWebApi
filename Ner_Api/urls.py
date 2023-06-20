from django.urls import path
from .views import ner_api

urlpatterns = [
    path('api/ner', ner_api, name='ner_api'),
]