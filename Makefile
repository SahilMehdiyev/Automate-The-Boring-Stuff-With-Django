PYTHON = $(PIPENV_RUN) python
DJANGO_MANAGE = $(PYTHON) manage.py

runserver:
	$(DJANGO_MANAGE) runserver

migrations:
	$(DJANGO_MANAGE) makemigrations

migrate:
	$(DJANGO_MANAGE) migrate

createsuperuser:
	$(DJANGO_MANAGE) createsuperuser

collectstatic:
	$(DJANGO_MANAGE) collectstatic --noinput

test:
	$(DJANGO_MANAGE) test

shell:
	$(DJANGO_MANAGE) shell

install:
	pip install -r requirements.txt

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down