import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from account.models import Transaction
from account.serializers import TransactionSerializer


def current_balance_view(request):
    data = {'balance': 0}
    for transaction in Transaction.objects.all():
        if transaction.type == Transaction.Type.INCOME:
            data['balance'] += transaction.amount
        else:
            data['balance'] -= transaction.amount

    return HttpResponse(json.dumps(data))


@api_view(['GET'])
def transaction_list_view(request):
    serializer = TransactionSerializer(Transaction.objects.all(), many=True)
    return Response(data=serializer.data)


class TransactionView(APIView):
    def get(self, request):
        serializer = TransactionSerializer(Transaction.objects.all(), many=True)
        return Response(data=serializer.data)
