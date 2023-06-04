from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client
from .tasks import *


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_price = self.full_price

    def save(self, *args, **kwargs):
        if self.full_price != self.__full_price:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)

        return super().save(*args, **kwargs)


class Plan(models.Model):
    PLAN_TYPES = (
        ('Student', 'Student'),
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Ultra', 'Ultra')
    )
    type = models.CharField(choices=PLAN_TYPES, max_length=20, unique=True)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[MaxValueValidator])

    def __str__(self):
        return self.type

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        if self.discount_percent != self.__discount_percent:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)

        return super().save(*args, **kwargs)


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscriptions')
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.client}: {self.service} - {self.plan}"

