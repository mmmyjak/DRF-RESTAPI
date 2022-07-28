from rest_framework import serializers
from .models import Category, Things

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name"
        )

class ThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Things
        fields = (
            "name",
            "importance",
            "created",
            "deadline",
            "category",
            "category_name",
        )
