Задача: Необходимо разработать систему сбора информации.
Система должна состоять из 2-х компонентов:
* Сервер на базе django
* Клиент-демон для linux.
Клиент периодически отправляет данные на сервер. Сервер их сохраняет и отображает пользователю.

Требование к клиенту-демону:
* Работает на linux
* Каждые 10 секунд отправляет на сервер текущую утилизацию cpu в %

* Чтобы запустить сервер + клиент, нужно установить репозиторий на машину на базе ОС Linux
* Также, если джанго не установлен, нужно будет прописать в терминал pip install Django
* Для запуска сервера необходимо прописать python manage.py runserver 8001
* Для запуска клиента необходимо запустить файл daemon.py
----
Также я добавил dockerfile, но в силу того, что докер "из коробки" не может параллельно запустить сервер и клиент,
собрав и запустив образ, будет работать только сервер, в браузере его можно посмотреть по адресу 127.0.0.1:8001
