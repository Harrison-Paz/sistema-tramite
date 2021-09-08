from django.db import models
from django.contrib.auth.models import AbstractUser


class Register(models.Model):
    code = models.CharField(max_length=3)
    description = models.TextField()
    public = models.BooleanField(default=True)


class Document(models.Model):
    code = models.CharField(max_length=2)
    description = models.TextField()
    public = models.BooleanField(default=True)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)


class Requirement(models.Model):
    charge = models.CharField(max_length=20)
    optional = models.BooleanField(default=False)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    state = models.BooleanField(default=False)


class Type_requirement(models.Model):
    description = models.TextField()
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    requirement = models.ForeignKey(Requirement, on_delete=models.SET_NULL, null=True)


class User(AbstractUser):
    program = models.TextField()
    code = models.CharField(max_length=10)


class Process(models.Model):
    code = models.CharField(max_length=8)
    coment = models.TextField()
    state = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    type_requirement = models.ForeignKey(Type_requirement, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

