from django.contrib.auth.models import AbstractUser
from django.db import models

from bf_task.auth_app.managers import AppUserManager


class AppUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = AppUserManager()
    def __str__(self):
        return self.email