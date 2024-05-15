from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    education = models.CharField(max_length=150, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)  # Allow blank and null values
    status = models.CharField(default="notverified", max_length=50)
    log_status = models.CharField(verbose_name="Status", max_length=50, default="offline")
    lock = models.CharField(max_length=50, default='none')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
