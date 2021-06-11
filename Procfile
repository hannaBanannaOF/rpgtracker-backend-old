release: python manage.py migrate
web: daphne -p $PORT -b 0.0.0.0 rpg_tracker.asgi
worker: python manage.py runworker