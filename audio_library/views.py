from rest_framework import generics, viewsets

from . import models
from . import serializers

from base.permissions import IsAuthor

class GenreListAPIView(generics.ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    """CRUD
    """
    serializer_class = serializers.LicenseSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.License.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
