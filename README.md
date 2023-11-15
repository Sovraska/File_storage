# File Storage

Приложение хранения и загрузки файлов с последующей обработкой их через celery

## О проекте 

- Проект завернут в Docker-контейнерах;
    ```
    Redis, db, picasso, celery, proxy:
    ```
- Посмотреть можно [тут](http://158.160.83.68/api/upload/) (не актуально) 
    
  
## Стек технологий
- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Celery
- Redis

## Зависимости
- Перечислены в файле backend/requirements.txt


## Для запуска на собственном сервере
Предворительно скоприовав код на сервер ```git@github.com:Sovraska/File_storage.git```

1. Установите на сервере `docker` и `docker-compose`
2. Создайте файл в `/picasso/.env` Шаблон для заполнения файла находится в `/picasso/.env.example`
3. Из корневой директории выполните команду `docker-compose up -d --build`
5. Можете создать учётную запись Администратора `docker-compose exec -it picasso python manage.py createsuperuser`
6. После чего по адресу <http://51.250.100.232/api/upload/> можно будет загрузить файлы.
7. А по адресу <http://51.250.100.232/api/files/> получить все файлы находящиеся на проекте

так же есть unittests выполнить на сервере их можно командой:

  ```sudo docker exec -it picasso pytest files/tests/tests.py```


## Автор

- [Семён Новиков](https://github.com/Sovraska) 
