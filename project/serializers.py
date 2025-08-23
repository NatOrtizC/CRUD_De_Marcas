from uuid import uuid4
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'brand', 'holder', 'registration_number', 'country', 'status', 'createdAt', 'updateAt')
        read_only_fields = ('createdAt', 'updateAt', 'registration_number')
        
        
    def create(self, validated_data):
        if not validated_data.get('registration_number'):
            validated_data['registration_number'] = f'REG-{uuid4().hex[:8].upper()}'
        return super().create(validated_data)