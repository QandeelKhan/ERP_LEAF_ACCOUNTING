# Generated by Django 5.0.4 on 2024-04-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance_must_be',
            field=models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], default=None, max_length=150),
            preserve_default=False,
        ),
    ]