from rest_framework import generics

from appG7C4.models.user import User
from appG7C4.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    