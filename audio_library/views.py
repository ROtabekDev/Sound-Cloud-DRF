from rest_framework import generics

from . import models
from . import serializers

class GenreListAPIView(generics.ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
