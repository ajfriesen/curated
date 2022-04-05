

needed packages:

sudo apt-get install libpq-dev



# brick-flow

## Install django

```
python3 --version
Python 3.6.9
```

## Database stuff

### Create database and user

sudo su - postgres

psql

CREATE DATABASE brick_flow;

CREATE USER brick_flow WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE brick_flow TO brick_flow;


Add priviledge to create databases for tests:

```
ALTER USER brick_flow CREATEDB;
```


# notizen

docker-compose up

docker-compose run web python manage.py createsuperuser

docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate

https://www.youtube.com/watch?v=EX6Tt-ZW0so


# passwort
asdfasdfasdf