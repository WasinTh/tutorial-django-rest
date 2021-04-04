import datetime
from rest_framework import serializers
from account.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(default=datetime.datetime.now())
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'created', 'amount', 'note', 'type', 'type_display']
