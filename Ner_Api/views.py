from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NerEntitySerializer
from .ner_spacy import ner_spacy

@api_view(['POST'])
def ner_api(request):
    text = request.data['text']
    entities = ner_spacy(text)
    serialized_entities = []
    for entity, label in entities:
        serialized_entities.append({'text': entity, 'label': label})
    return Response(serialized_entities)