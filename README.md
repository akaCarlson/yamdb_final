# api_yamdb
В данном проекте реализованы api запросы GET, POST, PUT, PATCH, DELETE
Авторизация реализована через simplejwt Token (с подтверждением через email).
Обьекты: произведения (title), категории (category), жанры (genre), комментарии (comment), отзывы (review).
Инфраструктура реализована в докер-контейнерах:
- db - postgres:13.0-alpine
- web - python:3.7-slim
- nginx - nginx:1.21.3-alpine

## Как развернуть проект на локальной машине:
### Пререквизиты:
- Doker *(дистрибутивы и инструкции по установке: https://docs.docker.com/engine/install/)*

### 1. Клонировать репозиторий:
- git clone https://github.com/akaCarlson/infra_sp2.git

### 2. Cоздать и запустить контейнеры:
- В терминале перейти в папку \infra_sp2\infra
- Запустить команду: docker-compose up *(создает и запускает контейнеры)*
    Будут развернуты и запущены три контейнера:
        ✔ Container infra-db-1
        ✔ Container infra-web-1
        ✔ Container infra-nginx-1
- Провести первичную настройку и выполнить миграции:
    - В терминале из папки \infra_sp2\infra запустить команды:
        - docker-compose exec web python manage.py migrate *(создает структуру данных в БД)*
        - docker-compose exec web python manage.py createsuperuser *(создает суперпользователя)*
        - docker-compose exec web python manage.py collectstatic --no-input *(настраивает работы со статикой)*
- Сервис будет доступен на 80 порту
- Спецификация API: http://127.0.0.1/redoc/
- Консоль администратора: http://127.0.0.1/admin
- Email с кодом подтверждения для регистрации пользователей будут располагаться в контейнере web по адресу app/sent_emails. Для доступа к коду подтверждения, выполнить команды из папки \infra_sp2\infra:
    - docker-compose exec web bash *(подключиться к терминалу контейнера web)*
    - cd sent_emails
    - ls *(посмотреть все отправленные email)*
    - cat имя_файла *(посмотреть содержание нужного email)*
    - exit *(выйти из терминала контейнера)*

### 3. Работа с тестовыми данными:
- CSV с тестовыми данными расположены в папке \infra_sp2\api_yamdb\api_yamdb\static
- В терминале из папки \infra_sp2\infra запустить команды:
    - docker-compose exec web python manage.py runscript load *(загрузка тестовых данных)*
    - docker-compose exec web python manage.py runscript unload *(удаление ранее загруженных тестовых данных)*
    - docker-compose exec web python manage.py runscript unload --script-args all *(удаление ВСЕХ данных из БД, кроме УЗ суперюзера)*


## Некоторые примеры запросов к API:
###### 1.1. Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/
###### 1.2. Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email (функционал отправки не реализован, файлы с email складываются в папку app/sent_emails в контейнере web).
###### 1.3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
###### 2. GET, POST к произведениям /api/v1/titles/
###### 3. GET, POST к жанрам\ категориям /api/v1/genres/ \ /api/v1/categories/
###### 4. GET, POST к отзывам /api/v1/titles/1/reviews/
###### 5. GET, POST к комментариям /api/v1/titles/1/reviews/1/comments
###### 6. Документация по api доступна по ссылке http://127.0.0.1/redoc/
