from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import process_file


class File(models.Model):
    file = models.FileField(upload_to="files", verbose_name="Файл")
    uploaded_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания записи"
    )
    processed = models.BooleanField(default=False, verbose_name="Состояние обработки")

    def __str__(self):
        return f"id: {self.pk}"


@receiver(post_save, sender=File)
def file_post_save(sender, instance, created, **kwargs):
    if created:
        process_file.delay(instance.id)
