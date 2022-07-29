from rest_framework import serializers
from .models import Category, Things
from django.contrib.auth.models import User


class NameLinkField(serializers.RelatedField):
    
    def to_representation(self, value):
        return '%s - %s' % (value, value.name)

class CategorySerializer(serializers.ModelSerializer):
    things = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='things-detail')
    class Meta:
        model = Category
        fields = ['id', 'name', 'things']

class ThingsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Things
        fields = (
            "url",
            "name",
            "importance",
            "created",
            "deadline",
            "category",
            "category_name",
            "owner"
        )

class UserSerializer(serializers.ModelSerializer):
    things = NameLinkField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'things']