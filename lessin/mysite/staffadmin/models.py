from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

# python manage.py makemigrations 数据库更新准备
# python manage.py migrate 数据库更新
# python manage.py runserver 8111


class Publisher(models.Model):
    pub_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    publish = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Character(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
