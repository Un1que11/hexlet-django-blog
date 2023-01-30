dev:
		poetry run ./manage.py runserver

build:
		poetry build

install:
		poetry install

shell:
		poetry run ./manage.py shell

reinstall:
		pip install --user --force-reinstall dist/*.whl

start:
		poetry run gunicorn hexlet_django_blog.wsgi

