from django.contrib import admin
from account.models import Transaction, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_amount']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['created', 'type', 'amount', 'note']
    list_filter = ['type']
