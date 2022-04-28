from django.db import models


# Create your models here.

class Password(models.Model):
    url = models.CharField(max_length=200, blank=True, db_index=True)
    password = models.CharField(max_length=100, db_index=True)
    user = models.IntegerField(max_length=100, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)


class User(models.Model):
    login = models.CharField(max_length=100, db_index=True, unique=True)
    password = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)