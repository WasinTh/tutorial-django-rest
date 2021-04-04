from django.contrib import admin
from account.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['created', 'type', 'amount', 'note']
    list_filter = ['type']
