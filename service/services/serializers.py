from .models import *
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.user.username')
    plan = PlanSerializer()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ('service', 'client', 'plan', 'price', 'id')

    def get_price(self, instance):
        return instance.price
