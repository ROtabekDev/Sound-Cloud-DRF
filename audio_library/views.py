from rest_framework import generics, viewsets, parsers, views

from base.services import delete_old_file

from . import models
from . import serializers

from base.permissions import IsAuthor
from base.classes import MixedSerializer,  Pagination

from django.shortcuts import get_object_or_404

import os

from django.http import FileResponse
from django.http import Http404


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

class TrackListView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.AuthorTrackSerializer
    pagination_class = Pagination

class AuthorTrackListView(generics.ListAPIView):
    serializer_class = serializers.AuthorTrackSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return models.Track.objects.filter(user__id=self.kwargs.get('pk'))

    
class StreamingFileView(views.APIView):

    def set_play(self, track):
        track.plays_count += 1
        track.save()

    def get(self, request, pk):
        track = get_object_or_404(models.Track, id=pk)

        if os.path.exists(track.file.path):
            self.set_play(track)
            return FileResponse(open(track.file.path, 'rb'), filename=track.file.name) 
        else:
            return Http404


class DownloadTrackView(views.APIView):

    def set_download(self):
        self.track.download += 1
        self.track.save()

    def get(self, request, pk):
        self.track = get_object_or_404(models.Track, id=pk)

        if os.path.exists(self.track.file.path):
            self.set_download()
            return FileResponse(
                open(self.track.file.path, 'rb'), filename=self.track.file.name, as_attachment=True
                ) 
        else:
            return Http404



