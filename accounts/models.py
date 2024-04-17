from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from .choices import *
from django.db.models import Sum


class Account(MPTTModel):
    Balance_Nature = [
        ("DEBIT", "Debit"),
        ("CREDIT", "Credit")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    account_type = models.CharField(max_length=40, choices=Account_Types)
    currency = models.CharField(max_length=3, choices=Currency_Type)
    balance_must_be = models.CharField(max_length=6, choices=Balance_Nature)

    def __str__(self):
        return self.name

from django.db import models
from django.db.models import Sum

class AccountBalance(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='balance')
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_debit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_credit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    closing_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.account.name

    @classmethod
    def update_balance(cls, account):
        opening_balance = account.balance.opening_balance if hasattr(account, 'balance') else 0
        total_debit = JournalEntry.objects.filter(debit_account=account).aggregate(Sum('debit_amount'))['debit_amount__sum'] or 0
        total_credit = JournalEntry.objects.filter(credit_account=account).aggregate(Sum('credit_amount'))['credit_amount__sum'] or 0
        closing_balance = opening_balance + total_debit - total_credit

        if hasattr(account, 'balance'):
            account.balance.opening_balance = opening_balance
            account.balance.total_debit = total_debit
            account.balance.total_credit = total_credit
            account.balance.closing_balance = closing_balance
            account.balance.save()
        else:
            cls.objects.create(
                account=account,
                opening_balance=opening_balance,
                total_debit=total_debit,
                total_credit=total_credit,
                closing_balance=closing_balance
            )

    def get_entries(self):
        debit_entries = JournalEntry.objects.filter(debit_account=self.account)
        credit_entries = JournalEntry.objects.filter(credit_account=self.account)
        return {
            'debit_entries': debit_entries,
            'credit_entries': credit_entries
        }

    def calculate_balance(self):
        total_debit = self.total_debit
        total_credit = self.total_credit
        balance = total_debit - total_credit
        return balance

class JournalEntry(models.Model):
    debit_account = models.ForeignKey(Account, related_name='debit_entries', on_delete=models.CASCADE)
    debit_particulars = models.CharField(max_length=255)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2)

    credit_account = models.ForeignKey(Account, related_name='credit_entries', on_delete=models.CASCADE)
    credit_particulars = models.CharField(max_length=255)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return self.debit_particulars

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update debit account balance
        debit_balance = self.debit_account.balance
        debit_balance.total_debit += self.debit_amount
        debit_balance.closing_balance += self.debit_amount
        debit_balance.save()

        # Update credit account balance
        credit_balance = self.credit_account.balance
        credit_balance.total_credit += self.credit_amount
        credit_balance.closing_balance -= self.credit_amount
        credit_balance.save()

