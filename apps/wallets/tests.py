from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.wallets.models import Wallet
from apps.wallets.serializers import WalletSerializer


class WalletListViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet_data = {
            'label': 'Test Wallet',
            'balance': 1000.0
        }
        self.wallet = Wallet.objects.create(**self.wallet_data)

    def test_get_wallet_list(self):
        response = self.client.get('/api/wallets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        self.assertEqual(response.data, serializer.data)


class WalletDetailViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet_data = {
            'label': 'Test Wallet',
            'balance': 1000.0
        }
        self.wallet = Wallet.objects.create(**self.wallet_data)

    def test_get_wallet_detail(self):
        response = self.client.get(f'/api/wallets/{self.wallet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = WalletSerializer(self.wallet)
        self.assertEqual(response.data, serializer.data)


class WalletCreateViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet_data = {
            'label': 'New Wallet',
            'balance': 500.0
        }

    def test_create_wallet(self):
        response = self.client.post('/api/wallets/create/', self.wallet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
