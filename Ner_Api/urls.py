from django.urls import path
from .views import ner_api, ner_apidf, ner_api_csv

urlpatterns = [
    path('api/ner', ner_api, name='ner_api'),
    path('api/nerdf', ner_apidf, name='ner_apidf'),
    path('api/nercsv', ner_api_csv, name='ner_api_csv'),
]