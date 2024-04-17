from django.db import models


class Account_Types(models.TextChoices):
    ASSETS = "ASSETS", "Assets"
    LIABILITIES = "LIABILITIES", "Liabilities"
    EQUITY = "EQUITY", "Equity"
    REVENUE = "REVENUE", "Revenue"
    EXPENSES = "EXPENSES", "Expenses"

class Transaction_Type(models.TextChoices):
    ATM_DEBIT_TRANSACTION = "ATM_DEBIT_TRANSACTION", "ATM and Debit Card Transaction"
    RTGS = "RTGS", "Real-Time Gross Settlement (RTGS)"
    IBFT = "IBFT", "Inter Bank Funds Transfers (IBFT)"
    DEPOSIT_BANK_CHECK = "DEPOSIT_BANK_CHECK", "Deposit Bank Check"
    PAY_ORDER = "PAY_ORDER", "Pay Order"
    DEMAND_DRAFT = "DEMAND_DRAFT", "Demand Draft"
    CASH_DEPOSIT = "CASH_DEPOSIT", "Cash Deposit"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL", "Cash Withdrawal"

    # Calculate the maximum length of choices
max_length = max(len(choice[1]) for choice in Transaction_Type.choices)

print("Maximum length of choices:", max_length)

class Currency_Type(models.TextChoices):
    PKR = "PKR", "Pakistani Rupee"
    USD = "USD", "US Dollar"
    INR = "INR", "Indian Rupee"
    EUR = "EUR", "Euro"
    GBP = "GBP", "British Pound Sterling"
    JPY = "JPY", "Japanese Yen"
    AUD = "AUD", "Australian Dollar"
