## Домашнее задание 3

### Настроить nginx для отдачи статический файлов из public/
Для выполнения ДЗ необходимо установить gunicorn и nginx.
Nginx должен быть установлен как системный пакет, а gunicorn как python библиотека в virtualenv.

В nginx нужно создать виртуальный хост и настроить его на отдачу файлов из директории /home/username/projectname/public.
Настройки nginx (точнее фрагмент содержащий вирт.хост) нужно положить в директорию проекта, что бы преподаватели могли его проверить.

### Создать простейшее WSGI приложение и запустить его с помощью gunicorn
Далее нужно создать простое WSGI приложение (без использования Flask или других фреймворков).
Приложение должно возвращать JSON документ с правильным MIME типом и содержимым вида {"time": <текущее время>, "url": <request url>}.
Запустить [gunicorn](https://docs.gunicorn.org/en/stable/run.html) и проверить работу приложения из браузера.

### Настроить проксирование запросов на nginx
Далее настроить Nginx для проксирования запросов к Gunicorn.
Отличать запросы которые нужно проксировать от тех которые нужно отдавать с диска можно по префиксу URL.
Все URL начинающиеся с API нужно проксировать на Gunicorn.

### Измерить производительность Nginx и Gunicorn c помощью ab или wrk. Добиться отказа системы
Протестировать производительность Nginx и Gunicorn c помощью утили ab (пакет apache2-utils) или wrk.
При тестировании нужно использовать минимум 4 потока и 5000 запросов.
Протестировать:
- отдачу статики Nginx;
- отдачу динамических документов Gunicorn;
- отдачу динамических документов Gunicorn при проксировании через Nginx;
- подобрать параметры, которые приведут к отказу системы;

