from tkinter import CASCADE
from django.core.validators import FileExtensionValidator
from django.db import models

from base.services import get_path_upload_avatar, validate_size_image


class AuthUser(models.Model):
    """Foydalanuvchi uchun model
    """
    email = models.EmailField('Email', max_length=150, unique=True)
    join_date = models.DateTimeField('Qo`shilgan vaqti', auto_now_add=True)
    country = models.CharField('Mamlakat', max_length=40, blank=True, null=True)
    city = models.CharField('Shahar', max_length=40, blank=True, null=True)
    bio = models.TextField('Bio', max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=40, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True, 
        null=True,
        validators = [FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

class Follower(models.Model):
    """Obunachi modeli
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscripber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscripber} {self.user} ning obuna bo`lgan'

    class Meta:
        verbose_name = 'Obunachi'
        verbose_name_plural = 'Obunachilar'

class SocialLink(models.Model):
    """Ijtimoiy tarmoqdagi sahifalari uchun model
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Linklar'