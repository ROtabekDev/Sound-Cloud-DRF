from django.core.exceptions import ValidationError

def get_path_upload_avatar(instance, file):
    """Media fayl manzili, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    """Faylning hajmini tekshirish
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"{megabyte_limit}MB dan oshmasligi kerak")