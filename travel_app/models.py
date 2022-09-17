from django.db import models
from django.contrib.auth.models import AbstractUser


# Main User Account Model - for customer and admin
class User(AbstractUser):

    # set metadata
    class Meta:
        db_table = "user"

    # User Types
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
