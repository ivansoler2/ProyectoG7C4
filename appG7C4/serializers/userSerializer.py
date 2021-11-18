from rest_framework import serializers
from appG7C4.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','name','product','document']


