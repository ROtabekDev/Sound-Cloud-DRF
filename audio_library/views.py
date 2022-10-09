from rest_framework import generics, viewsets, parsers

from base.services import delete_old_file

from . import models
from . import serializers

from base.permissions import IsAuthor
from base.classes import MixedSerializer

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

class AlbumViewSet(viewsets.ModelViewSet):
    """CRUD
    """
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.AlbumSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()

class PublicAlbumView(generics.ListAPIView):
    serializer_class = serializers.AlbumSerializer

    def get_queryset(self):
        return models.Album.objects.filter(user__id=self.kwargs.get('pk'), private=False)

class TrackView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD Track
    """
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = serializers.CreateAuthorTrackSerializer
    serializer_class_by_action = {
        'list': serializers.AuthorTrackSerializer
    }

    def get_queryset(self):
        return models.Track.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.file.path)
        instance.delete()

class PlayListView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD
    """
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = serializers.CreatePlayListSerializer
    serializer_class_by_action = {
        'list': serializers.PlayListSerializer
    }

    def get_queryset(self):
        return models.Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()
