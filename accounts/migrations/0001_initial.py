# Generated by Django 5.0.4 on 2024-04-17 14:28

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
                ('account_type', models.CharField(choices=[('Accumulated Depreciation', 'Accumulated Depreciation'), ('Asset Received But Not Billed', 'Asset Received But Not Billed'), ('Bank', 'Bank'), ('Cash', 'Cash'), ('Chargeable', 'Chargeable'), ('Capital Work in Progress', 'Capital Work in Progress'), ('Cost of Goods Sold', 'Cost of Goods Sold'), ('Depreciation', 'Depreciation'), ('Equity', 'Equity'), ('Expense Account', 'Expense Account'), ('Expenses Included in Asset Valuation', 'Expenses Included in Asset Valuation'), ('Fixed Asset', 'Fixed Asset'), ('Income Account', 'Income Account'), ('Payable', 'Payable'), ('Receivable', 'Receivable'), ('Round Off', 'Round Off'), ('Stock', 'Stock'), ('Stock Adjustment', 'Stock Adjustment'), ('Stock Received But Not Billed', 'Stock Received But Not Billed'), ('Service Received But Not Billed', 'Service Received But Not Billed'), ('Tax', 'Tax'), ('Temporary', 'Temporary')], max_length=40)),
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
            name='AccountBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('total_debit', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('total_credit', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('closing_balance', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='balance', to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_particulars', models.CharField(max_length=255)),
                ('debit_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credit_particulars', models.CharField(max_length=255)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_entries', to='accounts.account')),
                ('debit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_entries', to='accounts.account')),
            ],
        ),
    ]
