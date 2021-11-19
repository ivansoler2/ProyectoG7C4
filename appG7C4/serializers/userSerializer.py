from rest_framework import serializers
from appG7C4.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'name',
            'document', 
            'email',
            'city',
            'address',
            'phone',
            'image'
        ]


