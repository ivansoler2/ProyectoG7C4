# Create a serializer for the Publication model
from rest_framework import serializers
from ..models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title', 'description', 'date', 'image', 'category', 'user_id')