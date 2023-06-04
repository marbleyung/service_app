from .models import *
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.user.username')

    class Meta:
        model = Subscription
        fields = ('service', 'client', 'plan', 'id')


