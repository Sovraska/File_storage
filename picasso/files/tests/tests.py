import os
import shutil
import tempfile
from http import HTTPStatus

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picasso.settings")
import django
django.setup()
from django.conf import settings
from django.core.cache import cache
from django.test import Client, TestCase, override_settings

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)  # Создаём временную директорию
class PostViewTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """Создаём клиента и имя тестового файла"""
        super().setUpClass()

        cls.guest_client = Client()

        cls.file_name = "./test.jpg"

    def setUp(self):
        """Перед каждым тестом чистим кеш"""
        cache.clear()

    @classmethod
    def tearDownClass(cls):
        """После окончания работы удаляем временную директорию"""
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_submit_file(self):
        """Проверка отправки на сервер"""
        my_dir = os.path.dirname(__file__)
        file_dir = os.path.join(my_dir, self.file_name)
        with open(file_dir, "rb") as file:
            data = {"file": file}
            response = self.guest_client.post("http://127.0.0.1/api/upload/", data=data)
            self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_get_files(self):
        """Проверка ответа от сервера"""
        my_dir = os.path.dirname(__file__)
        file_dir = os.path.join(my_dir, self.file_name)
        # создаём 2 объекта в бд
        with open(file_dir, "rb") as file:
            data = {"file": file}
            response1 = self.guest_client.post(
                "http://127.0.0.1/api/upload/", data=data
            )
            self.assertEqual(response1.status_code, HTTPStatus.CREATED)

        with open(file_dir, "rb") as file:
            data = {"file": file}
            response2 = self.guest_client.post(
                "http://127.0.0.1/api/upload/", data=data
            )

            self.assertEqual(response2.status_code, HTTPStatus.CREATED)

        response = self.guest_client.get(
            "http://127.0.0.1/api/files/",
        )
        responses = response.json()
        example_fields = [
            "id",
            "file",
            "uploaded_at",
            "processed",
        ]
        for example_field in example_fields:
            self.assertEqual(len(responses), 2)
            for response in responses:
                self.assertTrue(example_field in response.keys())
