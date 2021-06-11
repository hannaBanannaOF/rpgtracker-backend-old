release: python manage.py migrate
web: daphne -p $PORT -b 0.0.0.0 rpgtracker.asgi:application
worker: python manage.py runworker -v2