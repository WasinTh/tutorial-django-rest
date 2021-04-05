import datetime
from rest_framework import serializers
from account.models import Transaction, Customer


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(default=datetime.datetime.now())
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
