import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from account.models import Transaction, Customer
from account.serializers import TransactionSerializer, CustomerSerializer


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


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
