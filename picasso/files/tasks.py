from celery import shared_task


@shared_task
def process_file(file_id):
    """Обработка файла"""
    from files.models import File

    file = File.objects.get(id=file_id)

    # Реализация обработки файла исходи из его типа

    file.processed = True
    file.save()
    return f"file with id:{file.id} processed."
