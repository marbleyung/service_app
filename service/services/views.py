from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from .serializers import *


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().\
        prefetch_related(
        Prefetch('client', queryset=Client.objects.all().\
                 select_related('user').\
                 only('company_name', 'user__username')
                 )
    ).\
        prefetch_related(
        'plan'
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response_data = {'result': response.data}
        response_data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
        response.data = response_data

        return response