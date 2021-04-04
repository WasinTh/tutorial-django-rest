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


def transaction_list_view(request):
    data = list()
    for transaction in Transaction.objects.all():
        data.append({
            'created': str(transaction.created),
            'amount': transaction.amount,
            'note': transaction.note,
            'type': transaction.type
        })

    return HttpResponse(json.dumps(data))
