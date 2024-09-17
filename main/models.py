from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Password(models.Model):
    url = models.CharField(max_length=200, blank=True, db_index=True)
    password = models.CharField(max_length=255, db_index=True)
    user = models.IntegerField(db_index=True)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AccauntUser(AbstractUser):
    username = models.CharField('login', max_length=100, db_index=True, unique=True)
    password = models.CharField('password', max_length=255, db_index=True)
    data = models.DateTimeField('data', auto_now_add=True)

    def __str__(self):
        return self.username

