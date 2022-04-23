Will come later


# notes

```
python manage.py runserver --settings landscape.settings.local
```


- https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/

- https://whitenoise.evans.io/en/stable/django.html

# Build and push to docker

```
source .github-package-token 
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker build -t ghcr.io/ajfriesen/landscape:latest . && docker push ghcr.io/ajfriesen/landscape:latest
```