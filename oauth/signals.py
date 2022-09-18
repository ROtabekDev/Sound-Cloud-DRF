from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import CustomUser, UserProfile 

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created: 
        user = instance  
        user_profile = UserProfile.objects.create(
                user = user
        ) 

@receiver(post_delete, sender=UserProfile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
 