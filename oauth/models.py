from django.core.validators import FileExtensionValidator
from django.db import models 

from base.services import get_path_upload_avatar, validate_size_image
 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, alias=None):
        user = self.model(
        email = self.normalize_email(email),
                username = username,)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', unique=True, error_messages={'unique':'Bu username mavjud.'}, max_length=50, null=True, blank=True)
    email = models.EmailField('Email',error_messages={'unique':'Bu email mavjud.'}, unique=True, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False) 

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Barcha foydalanuvchi'
        verbose_name_plural = 'Barcha foydalanuvchilar'

    def __str__(self): 
        return self.email


class UserProfile(models.Model):
    """Foydalanuvchi uchun model
    """
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    ) 
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
        return self.user.email
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

class Follower(models.Model):
    """Obunachi modeli
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    subscripber = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscripber} {self.user} ning obuna bo`lgan'

    class Meta:
        verbose_name = 'Obunachi'
        verbose_name_plural = 'Obunachilar'

class SocialLink(models.Model):
    """Ijtimoiy tarmoqdagi sahifalari uchun model
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Linklar'