from django.urls import path
from .views import ner_api, ner_apidf, ner_api_csv, process_person, save_entities

urlpatterns = [
    path('api/ner', ner_api, name='ner_api'),
    path('api/nerdf', ner_apidf, name='ner_apidf'),
    path('api/nercsv', ner_api_csv, name='ner_api_csv'),
    path('api/processperson', process_person, name='process_person'),
    path('api/save_entities', save_entities, name='save_entities'),
]