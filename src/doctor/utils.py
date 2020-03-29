"""Utility functions for doctor app."""

import os
import uuid

from django.conf import settings
from django.core.exceptions import ValidationError


def image_upload_util(instance, filename):
    """
    Renames the image and returns the upload path.
    
    It renames to image to a unique uuid.
    :instance: Instance whose image is to be renamed.
    :type instance: doctor.models.Doctor
    :filename: Filename of the image.
    :type filename: str
    :returns: Path where image is to be uploaded.
    :rtype: str
    """

    ext = filename.rpartition('.')[-1]
    image_uuid = str(uuid.uuid4())
    folder_name = settings.DOCTOR_DP_UPLOAD_FOLDER
    image_file_name = f'{image_uuid}.{ext}'
    return os.path.join(folder_name, image_file_name)


def image_file_size_validator(image):
    """Validates that the image size is not greater than the defined size."""

    file_size = image.size
    if file_size > settings.MAX_ALLOWED_IMAGE_SIZE_IN_MB * 1024 * 1024:
        raise ValidationError(
            f'Maximum allowed file size is {settings.MAX_ALLOWED_IMAGE_SIZE_IN_MB} MB.')
