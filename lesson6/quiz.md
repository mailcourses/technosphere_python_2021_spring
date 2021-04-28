# Квиз по ORM

1. В миграциях всегда указываются зависимости
- **Да**
- Нет

2. python manage.py makemigrations --empty yourappname
- Заменит последнюю миграцию на новую
- Отменит все примененные миграции
- **Создаст новую миграцию**
- Создаст фейковую миграцию

3. Для чего нужно apps.get_model('some_app', 'SomeModel')
- Для того, чтобы брать модели из кеша
- **Для того, чтобы избежать циклических импортов или импортировать модели тогда, когда они могут быть еще не доступны**
- Вообще так лучше делать всегда, когда хотим импортировать модель

4. Как сделать так, чтобы модель была доступна в админке
-  **admin.site.register(Chat, ChatAdmin)**
- admin.site.bind(Chat)
- register(ChatAdmin, admin=True)
- @admin.site.register

5. Какой метод отвечает за строковое представление модели в python3
- \_\_unicode\_\_
- \_\_repr\_\_
- **\_\_str\_\_**

6. class Meta отвечает за
- Конфигуцию приложения
- Конфигурацию полей модели
- **Конфигурацию модели**

7. Что такое "objects" в Tag.objects.create(slug=’some_tag’)?
- Model
- Queryset
- **ModelManager**
- Related Model Manager
- Object
- Метод экземпляра

8. Нужен ли save после post.tags.add(tag)
- Да
- **Нет**

9. Какое исключение, если объект не будет найден Post.objects.get(id=5) *
- **Post.DoesNotExist**
- DoesNotExist
- Posts.DoesNotExists
- NoObjectsReturned

10. Какой sql будет построен по запросу Post.objects.filter( title__contains='hello') *
- **SELECT "blog_post"."id", "blog_post"."title", "blog_post"."category_id", "blog_post"."author_id" FROM "blog_post" WHERE "blog_post"."title" LIKE %hello%**
- SELECT "blog_post"."id", "blog_post"."title", "blog_post"."category_id", "blog_post"."author_id" FROM "blog_post" WHERE "blog_post"."title" = hello
- SELECT "blog_post"."id", "blog_post"."title", "blog_post"."category_id", "blog_post"."author_id" FROM "blog_post" WHERE "blog_post"."title" IN (h, e, l, o)
- SELECT "blog_post"."id", "blog_post"."title", "blog_post"."category_id", "blog_post"."author_id" FROM "blog_post" INNER JOIN "blog_category" ON ("blog_post"."category_id" = "blog_category"."id") WHERE "blog_category"."title" LIKE %hello%

11. Какой объект вернется Post.objects.filter(category_id=1)
- **Queryset**
- List
- ModelManager

12. Что возвращает метод values_list?
- Список словарей с данными и описание колонок
- **Список кортежей с данными или только список полей**
- Список колонок

13. Post.objects.annotate(Count('tags'))
- Посчитает суммарное количество всех тегов
- **Посчитает количество тегов в каждом посте**
- Посчитает максимальное количество тегов в посте