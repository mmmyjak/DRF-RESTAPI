from django.urls import path, include
from things import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'things', views.ThingViewSet, basename="things")
router.register(r'done', views.DoneThingViewSet, basename="done")
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'categories', views.CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls)),
]
