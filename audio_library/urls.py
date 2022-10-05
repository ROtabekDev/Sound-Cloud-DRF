from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.GenreListAPIView.as_view(), name='genres'),

    path('license/', views.LicenseViewSet.as_view({'get': 'list', 'post': 'create'})), 
    path('license/<int:pk>/', views.LicenseViewSet.as_view({'put': 'update', "delete": 'destroy'})),

    path('album/', views.AlbumViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('album/<int:pk>/', views.AlbumViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]