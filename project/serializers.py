from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'brand', 'holder', 'registration_number', 'country', 'status', 'createdAt', 'updateAt')
        read_only_fields = ('createdAt',)