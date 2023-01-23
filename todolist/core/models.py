from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    email = models.EmailField(unique=True)

    # def __str__(self):
    #     return self.username

    
    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)

    #     super().save()


    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'
    #     ordering = ("username",)
