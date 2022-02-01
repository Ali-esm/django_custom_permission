from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    groups = models.ManyToManyField(to='UserGroup')

    def __str__(self):
        return f'{self.username}'


class Permission(models.Model):
    see_users = models.BooleanField()
    see_permissions = models.BooleanField()
    create_user = models.BooleanField()


class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(to=Permission)

    def __str__(self):
        return f'{self.name}'