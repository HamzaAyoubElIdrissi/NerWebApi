from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import HttpResponse
from .serializers import NerEntitySerializer
from .ner_spacy import ner_spacy
from .ner_spacy import extract_entities


@api_view(['POST'])
def ner_api(request):
    text = request.data['text']
    entities = ner_spacy(text)
    serialized_entities = []
    for entity, label in entities:
        serialized_entities.append({'text': entity, 'label': label})
    return Response(serialized_entities)


@api_view(['POST'])
def ner_apidf(request):
    text = request.data['text']
    df = extract_entities(text)    
    # Convert dataframe to JSON
    json_data = df.to_json(orient='records')
    return Response(json_data)



@api_view(['POST'])
def ner_api_csv(request):
    text = request.data['text']
    df = extract_entities(text)
    
    # Check if the dataframe is empty
    if df.empty:
        return Response({'message': 'No entities found.'}, status=status.HTTP_204_NO_CONTENT)
    
    # Convert the dataframe to CSV
    csv_data = df.to_csv(index=False)
    
    # Set the response content type as CSV
    response = HttpResponse(csv_data, content_type='text/csv')
    
    # Set the Content-Disposition header to trigger file download
    response['Content-Disposition'] = 'attachment; filename="entities.csv"'
    
    return response