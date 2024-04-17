from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(JournalEntry)


class AccountBalanceAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'total_credit', 'total_debit']

    def account_name(self, obj):
        return obj.account.name

    def total_debit(self, obj):
        return obj.total_debit

    def total_credit(self, obj):
        return obj.total_credit

admin.site.register(AccountBalance, AccountBalanceAdmin)