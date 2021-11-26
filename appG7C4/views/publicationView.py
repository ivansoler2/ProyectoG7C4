# Create a Publication view with generic views
from rest_framework import generics
from ..models import Publication
from ..serializers import PublicationSerializer

class PublicationListCreateView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class PublicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer