import datetime
from rest_framework import serializers
from account.models import Transaction


class TransactionSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(default=datetime.datetime.now())
    amount = serializers.IntegerField()
    note = serializers.CharField(required=False, allow_blank=True, default='')
    type = serializers.ChoiceField(choices=Transaction.Type)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)
