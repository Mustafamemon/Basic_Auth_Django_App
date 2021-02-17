from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

# os - Organzier and Service Provider
# gp - General Public
class User(AbstractUser):
    username  = models.CharField("username", max_length=50,unique=True ,null=True)
    is_gp = models.BooleanField(default=False , help_text="if user is a genral public")
    is_os  = models.BooleanField(default=False , help_text="if user is organzier and service provider")
    