from rest_framework import serializers

from . import models
from django.contrib.auth.hashers import make_password
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password')
    
    def validate_password(self, value: str) -> str: 
        return make_password(value)

class UserProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.UserProfile
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class SocialLinkSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.SocialLink
        fields=('id', 'link')

class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)
    class Meta:
        model = models.UserProfile
        fields = ('avatar', 'country', 'city', 'bio', 'display_name', 'social_links')

class GoogleAuth(serializers.Serializer):
    email = serializers.EmailField()
    toke = serializers.CharField()