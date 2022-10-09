from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.GenreListAPIView.as_view(), name='genres'),

    path('license/', views.LicenseViewSet.as_view({'get': 'list', 'post': 'create'})), 
    path('license/<int:pk>/', views.LicenseViewSet.as_view({'put': 'update', "delete": 'destroy'})),

    path('album/', views.AlbumViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('album/<int:pk>/', views.AlbumViewSet.as_view({'put': 'update', 'delete': 'destroy'})),

    path('author-album/<int:pk>/', views.PublicAlbumView.as_view()),

    path('track/', views.TrackView.as_view({'get': 'list', 'post': 'create'})),
    path('track/<int:pk>/', views.TrackView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('playlist/', views.PlayListView.as_view({'get': 'list', 'post':'create'})),
    path('playlist/<int:pk>/', views.PlayListView.as_view({'put': 'update', 'delete': 'destroy'})),
]