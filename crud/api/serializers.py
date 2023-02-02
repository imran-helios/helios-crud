from rest_framework import serializers
from crud.models import Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id','name', 'phone', 'photo']
        read_only_fields = ['id']
    
