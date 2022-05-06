release: python manage.py migrate
web: sh -c 'cd whatsaround && gunicorn whatsaround.wsgi --log-file=-'