from django.urls import path, include
from things import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('things/', views.ThingsList.as_view()),
    path('things/<int:pk>/', views.ThingsDetail.as_view()),
    # path('things/<str:cat>/', views.CategoryList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]