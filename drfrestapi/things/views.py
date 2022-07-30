from .models import Category, Thing
from .serializers import ThingSerializer, UserSerializer, CategorySerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().filter(done=False)
    serializer_class = ThingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DoneThingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Thing.objects.all().filter(done=True)
    serializer_class = ThingSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Thing.objects.all()
#     serializer_class = ThingSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# --------------- MIXINS --------------------------
# class ThingsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Things.objects.all()
#     serializer_class = ThingsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ThingsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Things.objects.all()
#     serializer_class = ThingsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# --------------- APIVIEW --------------------------
# class ThingsList(APIView):

#     def get(self, request, format=None):
#         things = Things.objects.all()
#         serializer = ThingsSerializer(things, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ThingsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ThingsDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Things.objects.get(pk=pk)
#         except Things.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         thing = self.get_object(pk)
#         serializer = ThingsSerializer(thing)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         thing = self.get_object(pk)
#         serializer = ThingsSerializer(thing, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         thing = self.get_object(pk)
#         thing.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryList(APIView):

#     def get_object(self, cat):
#         try:
#             category = Category.objects.get(name=cat.lower())
#             return Things.objects.all().filter(category=category.id)
#         except (Things.DoesNotExist, Category.DoesNotExist):
#             return Http404
    
#     def get(self, request, cat, format=None):
#         things = self.get_object(cat)
#         serializer = ThingsSerializer(things, many=True)
#         return Response(serializer.data)