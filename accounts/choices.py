from django.db import models


class Account_Types(models.TextChoices):
    # ASSETS = "ASSETS", "Assets"
    # LIABILITIES = "LIABILITIES", "Liabilities"
    # EQUITY = "EQUITY", "Equity"
    # REVENUE = "REVENUE", "Revenue"
    # EXPENSES = "EXPENSES", "Expenses"
    Accumulated_Depreciation = "Accumulated Depreciation", "Accumulated Depreciation"
    Asset_Received_But_Not_Billed = "Asset Received But Not Billed", "Asset Received But Not Billed"
    Bank = "Bank", "Bank"
    Cash = "Cash", "Cash"
    Chargeable = "Chargeable", "Chargeable"
    Capital_Work_in_Progress = "Capital Work in Progress", "Capital Work in Progress"
    Cost_of_Goods_Sold = "Cost of Goods Sold", "Cost of Goods Sold"
    Depreciation = "Depreciation", "Depreciation"
    Equity = "Equity", "Equity"
    Expense_Account = "Expense Account", "Expense Account"
    Expenses_Included_in_Asset_Valuation = "Expenses Included in Asset Valuation", "Expenses Included in Asset Valuation"
    Fixed_Asset = "Fixed Asset", "Fixed Asset"
    Income_Account = "Income Account", "Income Account"
    Payable = "Payable", "Payable"
    Receivable = "Receivable", "Receivable"
    Round_Off = "Round Off", "Round Off"
    Stock = "Stock", "Stock"
    Stock_Adjustment = "Stock Adjustment", "Stock Adjustment"
    Stock_Received_But_Not_Billed = "Stock Received But Not Billed", "Stock Received But Not Billed"
    Service_Received_But_Not_Billed = "Service Received But Not Billed", "Service Received But Not Billed"
    Tax = "Tax", "Tax"
    Temporary = "Temporary", "Temporary"


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
