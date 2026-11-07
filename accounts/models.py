from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class AccountType(models.TextChoices):
        GUEST = "guest", "Guest"
        HOST = "host", "Host"

    account_type = models.CharField(max_length=10, choices=AccountType.choices, default=AccountType.GUEST)
    is_verified = models.BooleanField(default=False)