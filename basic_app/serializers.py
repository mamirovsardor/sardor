from attr import fields
from rest_framework import serializers
from .import models


class ListApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ListApi
        fields='__all__'
        
class TaomApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TaomApi
        fields='__all__'