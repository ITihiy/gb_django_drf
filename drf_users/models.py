from django.contrib.auth.models import AbstractUser
from django.db import models


class DRFUser(AbstractUser):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField('email address', null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
