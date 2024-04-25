from django.db import models


class Transaction(models.Model):
    wallet = models.ForeignKey('wallets.Wallet', related_name='transactions', on_delete=models.CASCADE)
    txid = models.CharField(max_length=255, unique=True, db_index=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.txid
