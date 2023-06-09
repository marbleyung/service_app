from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} ({self.company_name})"
