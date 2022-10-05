from django.core.exceptions import ValidationError
import os

def get_path_upload_avatar(instance, file):
    """Media fayl manzili, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.pk}/{file}'


def get_path_upload_cover_album(instance, file):
    """Media fayl manzili, format: (media)/album/user_id/photo.jpg
    """
    return f'album/user_{instance.pk}/{file}'


def get_path_upload_cover_playlist(instance, file):
    """Media fayl manzili, format: (media)/playlist/user_id/photo.jpg
    """
    return f'playlist/user_{instance.pk}/{file}'


def get_path_upload_track(instance, file):
    """Audio fayl manzili, format: (media)/track/user_id/audio.mp3
    """
    return f'track/user_{instance.pk}/{file}'



def validate_size_image(file_obj):
    """Faylning hajmini tekshirish
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"{megabyte_limit}MB dan oshmasligi kerak")

def delete_old_file(path_file):
    """Eski faylini o'chirish
    """
    if os.path.exists(path_file):
        os.remove(path_file)