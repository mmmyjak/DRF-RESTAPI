from django.urls import path
from things import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('things/', views.ThingsList.as_view()),
    path('things/<int:pk>/', views.ThingsDetail.as_view()),
    path('things/<str:cat>/', views.CategoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)