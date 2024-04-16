from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Account_Types(models.TextChoices):
    ASSETS = "ASSETS", "Assets"
    LIABILITIES = "LIABILITIES", "Liabilities"
    EQUITY = "EQUITY", "Equity"
    REVENUE = "REVENUE", "Revenue"
    EXPENSES = "EXPENSES", "Expenses"

class Currency_Type(models.TextChoices):
    USD = "USD", "US Dollar"
    INR = "INR", "Indian Rupee"
    EUR = "EUR", "Euro"
    GBP = "GBP", "British Pound Sterling"
    JPY = "JPY", "Japanese Yen"
    AUD = "AUD", "Australian Dollar"
    CAD = "CAD", "Canadian Dollar"
    CHF = "CHF", "Swiss Franc"
    NZD = "NZD", "New Zealand Dollar"
    CNY = "CNY", "Chinese Yuan Renminbi"
    BRL = "BRL", "Brazilian Real"
    MXN = "MXN", "Mexican Peso"
    ZAR = "ZAR", "South African Rand"
    RUB = "RUB", "Russian Ruble"
    KRW = "KRW", "South Korean Won"
    SGD = "SGD", "Singapore Dollar"
    HKD = "HKD", "Hong Kong Dollar"
    SEK = "SEK", "Swedish Krona"
    NOK = "NOK", "Norwegian Krone"
    DKK = "DKK", "Danish Krone"



class Account(MPTTModel):
    name = models.CharField(max_length=100)
    # balance = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    # account_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    account_type = models.CharField(max_length=20, choices=Account_Types)
    currency = models.CharField(max_length=3, choices=Currency_Type)

    def __str__(self):
        return self.name

    # @property
    # def total_amount(self):
    #     return self.balance
    
    # def save(self, *args, **kwargs):
    #     # If account_id is not provided by the user, generate a unique ID
    #     if not self.account_id:
    #         # Generate a unique ID with IFTRX prefix and 2-3 digits
    #         self.account_id = 'IFTRX' + str(uuid.uuid4().fields[-1])[:3]
    #     super().save(*args, **kwargs)


class Transaction_Type(models.TextChoices):
    ATM_DEBIT_TRANSACTION = "ATM_DEBIT_TRANSACTION", "ATM and Debit Card Transaction"
    RTGS = "RTGS", "Real-Time Gross Settlement (RTGS)"
    IBFT = "IBFT", "Inter Bank Funds Transfers (IBFT)"
    DEPOSIT_BANK_CHECK = "DEPOSIT_BANK_CHECK", "Deposit Bank Check"
    PAY_ORDER = "PAY_ORDER", "Pay Order"
    DEMAND_DRAFT = "DEMAND_DRAFT", "Demand Draft"
    CASH_DEPOSIT = "CASH_DEPOSIT", "Cash Deposit"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL", "Cash Withdrawal"
    
class Transaction(models.Model):
    # --dirty field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # --dirty field
    # reason = models.CharField(max_length=30, choices=TransactionReason)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(_("Transaction_Type"), max_length=100, choices=Transaction_Type.choices
    )
    # transaction_medium = models.CharField(_("Transaction_Medium"), max_length=20, choices=TransactionMedium.choices, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.date}-{self.description}'
    
    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"
