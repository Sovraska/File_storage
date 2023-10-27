from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = (
        "file",
        "uploaded_at",
        "processed",
    )
    list_display = (
        "id",
        "file",
        "uploaded_at",
        "processed",
    )
