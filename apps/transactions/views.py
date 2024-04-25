from utils.mixins import ExecutionTimeLimitMixin, MemoryUsageLimitMixin
from .models import Transaction
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .services import create_transaction
from .serializers import TransactionSerializer


class TransactionListView(ExecutionTimeLimitMixin, MemoryUsageLimitMixin, generics.ListAPIView):
    queryset = Transaction.objects.select_related('wallet')
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['txid']
    ordering_fields = ['amount', 'id']


class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        wallet_id = serializer.validated_data.get('wallet_id')
        txid = serializer.validated_data.get('txid')
        amount = serializer.validated_data.get('amount')

        try:
            transaction = create_transaction(wallet_id, txid, amount)
            serialized_transaction = TransactionSerializer(transaction)
            return Response(serialized_transaction.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Failed to create transaction. Please try again later.'},
                            status=status.HTTP_400_BAD_REQUEST)
