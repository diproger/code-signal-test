from django.db import transaction
from .models import Transaction
from apps.wallets.models import Wallet


def create_transaction(wallet_id, txid, amount):
    with transaction.atomic():
        trans = Transaction.objects.create(wallet_id=wallet_id, txid=txid, amount=amount)
        wallet = Wallet.objects.get(id=wallet_id)
        wallet.update_balance()
        return trans
