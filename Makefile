# Define Python and Django management commands
PYTHON = poetry run python
DJANGO_MANAGE = $(PYTHON) manage.py

# Django commands
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

# Install dependencies
install:
	poetry install

# Docker commands
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

# Celery commands
celery-worker:
	poetry run celery -A awd_main worker --loglevel=info

celery-beat:
	poetry run celery -A awd_main beat --loglevel=info

celery-flower:
	poetry run celery -A awd_main flower

# Clean up
clean-pyc:
	find . -name "*.pyc" -o -name "*.pyo" -delete

clean-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
