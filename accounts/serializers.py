from rest_framework import serializers
from .models import Teacher

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Teacher.objects.create_user(**validated_data)
        return user
