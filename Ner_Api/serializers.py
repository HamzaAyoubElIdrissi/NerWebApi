from rest_framework import serializers
from .models import NerEntity

class NerEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NerEntity
        fields = ('text', 'label')
        