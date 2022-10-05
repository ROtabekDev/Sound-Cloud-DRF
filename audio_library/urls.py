from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.GenreListAPIView.as_view(), name='genres'),
]