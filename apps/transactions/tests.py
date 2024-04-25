from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from apps.wallets.models import Wallet


class TransactionListViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=1000.0)
        self.transaction_data = {
            'wallet_id': self.wallet.id,
            'txid': 'abc123',
            'amount': 100.0
        }
        self.transaction = Transaction.objects.create(**self.transaction_data)

    def test_get_transaction_list(self):
        response = self.client.get('/api/transactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        self.assertEqual(response.data, serializer.data)


class TransactionDetailViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=1000.0)
        self.transaction_data = {
            'wallet_id': self.wallet.id,
            'txid': 'abc123',
            'amount': 100.0
        }
        self.transaction = Transaction.objects.create(**self.transaction_data)

    def test_get_transaction_detail(self):
        response = self.client.get(f'/api/transactions/{self.transaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TransactionSerializer(self.transaction)
        self.assertEqual(response.data, serializer.data)


class TransactionCreateViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=1000.0)
        self.transaction_data = {
            'wallet_id': self.wallet.id,
            'txid': 'abc123',
            'amount': 100.0
        }

    def test_create_transaction(self):
        response = self.client.post('/api/transactions/create/', self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)
