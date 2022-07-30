from rest_framework import serializers
from .models import Category, Thing
from django.contrib.auth.models import User




class CategorySerializer(serializers.ModelSerializer):
    things = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='things-detail')
    class Meta:
        model = Category
        fields = ['id', 'name', 'things']

class ThingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name="things-detail")
    class Meta:
        model = Thing
        fields = (
            "id",
            "name",
            "importance",
            "created",
            "deadline",
            "category",
            "category_name",
            "owner",
            "done",
            "url"
        )


class NameBoolField(serializers.RelatedField):
    def to_representation(self, value):
        return '%s - DONE: %s' % (value, value.done)
        
class UserSerializer(serializers.ModelSerializer):
    things = NameBoolField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'things']