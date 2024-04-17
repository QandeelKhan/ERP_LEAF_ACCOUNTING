from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from .choices import *


class Account(MPTTModel):
    Balance_Nature = [
        ("DEBIT", "Debit"),
        ("CREDIT", "Credit")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    account_type = models.CharField(max_length=20, choices=Account_Types)
    currency = models.CharField(max_length=3, choices=Currency_Type)
    balance_must_be = models.CharField(max_length=6, choices=Balance_Nature)
    # rate at which this tax applies: The field rate_at_which_this_tax_applies in an accounting system is typically used to store the percentage rate of a particular tax that applies to a transaction or an account. This could be for various taxes like sales tax, value-added tax (VAT), or any other applicable taxes. The rate is crucial for calculating the tax amount that needs to be applied to a transaction.
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text=_('The tax rate (in percentage %) applicable to the account'))

    def __str__(self):
        return self.name

class Transaction(models.Model):
    # --dirty field
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # --dirty field
    # reason = models.CharField(max_length=30, choices=TransactionReason)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(_("Transaction_Type"), max_length=50, choices=Transaction_Type.choices
    )
    # transaction_medium = models.CharField(_("Transaction_Medium"), max_length=20, choices=TransactionMedium.choices, null=True, blank=True)
    
    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"

    def calculate_tax(self):
        # This will calculate 5% of the transaction amount
        tax_amount = (self.amount * self.account.tax_rate) / 100
        return tax_amount
