from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()


class Plan(models.Model):
    PLAN_TYPES = (
        ('Student', 'Student'),
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Ultra', 'Ultra')
    )
    type = models.CharField(choices=PLAN_TYPES, max_length=20)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[MaxValueValidator])


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscriptions')
