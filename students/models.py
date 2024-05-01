from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    age = models.IntegerField(default=7)
    grade = models.IntegerField(default=1)
