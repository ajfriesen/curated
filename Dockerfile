FROM python:3.10.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# User and group to run the app
ARG APP_USER=landscape
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# Install package needed for the application
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  postgresql-client && \
  apt-get clean

RUN mkdir /requirements
ADD requirements /requirements

# Install build dependencies for pip
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  libpq-dev && \
  apt-get clean

RUN pip install -r /requirements/prod.txt && \
  pip cache purge

# Copy code
RUN mkdir /code
WORKDIR /code
COPY . /code/

# gunicorn will listen on this port
EXPOSE 8000

# Add any static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=landscape.settings.prod

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN python manage.py collectstatic --noinput

# Change to a non-root user
# USER ${APP_USER}:${APP_USER}

ENTRYPOINT ["./entrypoint.sh"]

# Start uWSGI
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "landscape.wsgi:application"]
