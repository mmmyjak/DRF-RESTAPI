from rest_framework import serializers
from .models import Category, Things

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )

class ThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Things
        fields = '__all__'