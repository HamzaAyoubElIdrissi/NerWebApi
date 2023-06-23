from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import HttpResponse
from .serializers import NerEntitySerializer
from .ner_spacy import ner_spacy
from .ner_spacy import extract_entities
from .ner_spacy import get_entity_description
from .ner_spacy import summarize_text
from .models import PersonEntity, MoneyEntity, LocEntity, GpeEntity, OrgEntity


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



@api_view(['POST'])
def process_person(request):
    text = request.data['text']
    df = extract_entities(text)
    
    # Get the list of person entities
    person_entities = df['PERSON'].iloc[0]
    
    # Iterate through the person entities
    for person in person_entities:
        # Check if the person already exists in the database
        if not Person.objects.filter(person=person).exists():
            # Create a new person object
            new_person = Person(person=person, descript="")
            new_person.save()
    
    return Response({'message': 'Person entities processed successfully.'})


@api_view(['POST'])
def save_entities(request):
    text = request.data['text']
    df = extract_entities(text)

    entity_types = ['PERSON', 'MONEY', 'LOC', 'GPE', 'ORG']
    entity_models = {
        'PERSON': PersonEntity,
        'MONEY': MoneyEntity,
        'LOC': LocEntity,
        'GPE': GpeEntity,
        'ORG': OrgEntity
    }

    for entity_type in entity_types:
        entities = df[entity_type].iloc[0]

        for entity in entities:
            if not entity_models[entity_type].objects.filter(**{entity_type.lower(): entity}).exists():
                description = get_entity_description(entity)
                summary = summarize_text(description)
                
                new_entity = entity_models[entity_type](**{entity_type.lower(): entity, 'description': description, 'summarized_description': summary})
                new_entity.save()

    return Response({'message': 'Entities processed successfully.'})
