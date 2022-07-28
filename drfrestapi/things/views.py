from .models import Category, Things
from .serializers import ThingsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ThingsList(APIView):

    def get(self, request, format=None):
        things = Things.objects.all()
        serializer = ThingsSerializer(things, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ThingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThingsDetail(APIView):

    def get_object(self, pk):
        try:
            return Things.objects.get(pk=pk)
        except Things.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        thing = self.get_object(pk)
        serializer = ThingsSerializer(thing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        thing = self.get_object(pk)
        serializer = ThingsSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        thing = self.get_object(pk)
        thing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):

    def get_object(self, cat):
        try:
            category = Category.objects.get(name=cat.lower())
            return Things.objects.all().filter(category=category.id)
        except (Things.DoesNotExist, Category.DoesNotExist):
            return Http404
    
    def get(self, request, cat, format=None):
        things = self.get_object(cat)
        serializer = ThingsSerializer(things, many=True)
        return Response(serializer.data)