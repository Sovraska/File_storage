from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from picasso.settings import ALLOWED_FILE_TYPES

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("id", "file", "uploaded_at", "processed")

    def validate(self, attrs):
        file_type = attrs.get("file")
        if file_type:
            file_type = file_type.content_type
        if file_type not in ALLOWED_FILE_TYPES:
            print(file_type)
            raise ValidationError("Этот тип файла не доступен")
        return attrs
