from django.db import models
from django.db.models import Sum


class Wallet(models.Model):
    label = models.CharField(max_length=255, db_index=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, editable=False, default=0)

    def update_balance(self):
        self.balance = self.transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        self.save()

    def __str__(self):
        return self.label
