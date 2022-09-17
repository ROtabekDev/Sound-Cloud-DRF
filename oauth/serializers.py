from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    email = serializers.EmailField()
    toke = serializers.CharField()