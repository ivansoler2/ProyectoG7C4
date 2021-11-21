from django.db.models import query
from rest_framework import generics

from appG7C4.models.user import User
from appG7C4.serializers.userSerializer import UserSerializer

class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    