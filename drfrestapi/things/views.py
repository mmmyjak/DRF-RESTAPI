from .models import Category, Thing
from .serializers import ThingSerializer, UserSerializer, CategorySerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ThingViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        if self.action == 'list':
            return Thing.objects.all().filter(done=False)
        else:
            return Thing.objects.all()

    serializer_class = ThingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DoneThingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Thing.objects.all().filter(done=True)
    serializer_class = ThingSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
