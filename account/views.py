import json
from django.http import HttpResponse
from account.models import Transaction


def current_balance_view(request):
    data = {'balance': 0}
    for transaction in Transaction.objects.all():
        if transaction.type == Transaction.Type.INCOME:
            data['balance'] += transaction.amount
        else:
            data['balance'] -= transaction.amount

    return HttpResponse(json.dumps(data))
