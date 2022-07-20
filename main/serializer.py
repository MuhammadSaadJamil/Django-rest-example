from rest_framework import serializers
from .models import *


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'


class RelatedObjectSerializer(ObjectSerializer):
    ingredients = ObjectSerializer(read_only=False, many=True)
