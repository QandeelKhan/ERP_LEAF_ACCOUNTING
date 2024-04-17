# Generated by Django 5.0.4 on 2024-04-17 06:29

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('account_type', models.CharField(choices=[('ASSETS', 'Assets'), ('LIABILITIES', 'Liabilities'), ('EQUITY', 'Equity'), ('REVENUE', 'Revenue'), ('EXPENSES', 'Expenses')], max_length=20)),
                ('currency', models.CharField(choices=[('PKR', 'Pakistani Rupee'), ('USD', 'US Dollar'), ('INR', 'Indian Rupee'), ('EUR', 'Euro'), ('GBP', 'British Pound Sterling'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar')], max_length=3)),
                ('balance_must_be', models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], max_length=6)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounts.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('ATM_DEBIT_TRANSACTION', 'ATM and Debit Card Transaction'), ('RTGS', 'Real-Time Gross Settlement (RTGS)'), ('IBFT', 'Inter Bank Funds Transfers (IBFT)'), ('DEPOSIT_BANK_CHECK', 'Deposit Bank Check'), ('PAY_ORDER', 'Pay Order'), ('DEMAND_DRAFT', 'Demand Draft'), ('CASH_DEPOSIT', 'Cash Deposit'), ('CASH_WITHDRAWAL', 'Cash Withdrawal')], max_length=50, verbose_name='Transaction_Type')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
