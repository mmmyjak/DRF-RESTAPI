from rest_framework import serializers
from .models import Category, Things
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name"
        )

class ThingsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Things
        fields = (
            "name",
            "importance",
            "created",
            "deadline",
            "category",
            "category_name",
            "owner"
        )

class UserSerializer(serializers.ModelSerializer):
    things = serializers.PrimaryKeyRelatedField(many=True, queryset=Things.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'things']