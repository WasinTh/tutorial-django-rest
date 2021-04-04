from django.http import HttpResponse
from account.models import Transaction


def current_balance_view(request):
    balance = 0
    for transaction in Transaction.objects.all():
        if transaction.type == Transaction.Type.INCOME:
            balance += transaction.amount
        else:
            balance -= transaction.amount

    return HttpResponse(f"{balance} บาท")
