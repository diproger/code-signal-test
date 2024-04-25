from rest_framework import generics, filters
from django.db import transaction

from utils.mixins import ExecutionTimeLimitMixin, MemoryUsageLimitMixin
from .models import Wallet
from .serializers import WalletSerializer


class WalletListView(ExecutionTimeLimitMixin, MemoryUsageLimitMixin, generics.ListAPIView):
    queryset = Wallet.objects.prefetch_related('transactions')
    serializer_class = WalletSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['balance', 'id']


class WalletDetailView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletCreateView(generics.CreateAPIView):
    serializer_class = WalletSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
