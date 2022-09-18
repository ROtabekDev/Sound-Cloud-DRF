from django.contrib import admin
from .models import CustomUser, UserProfile, Follower, SocialLink
 
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('email',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'display_name', 'join_date')
    list_display_links = ('email',)

    def email(self, obj):
        return obj.user.email


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscripber') 

    
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link') 
