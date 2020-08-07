from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_shopowner = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=10)

    REQUIRED_FIELDS = ["mobile_no", "date_of_birth"]
