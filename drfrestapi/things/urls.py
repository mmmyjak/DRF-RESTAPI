from django.urls import path
from things import views

urlpatterns = [
    path('things/', views.things_list),
    path('things/<int:pk>/', views.things_detail),
    path('things/<str:cat>/', views.category_list),
]
