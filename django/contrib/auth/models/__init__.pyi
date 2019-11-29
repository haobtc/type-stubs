from django.db import models

class Permission(models.Model):
    pass

class User(models.Model):
    email: models.CharField

    def has_perm(self, perm:'Permission') -> bool: ...

class Group(models.Model):
    ...
