from django.test import TestCase
from account.models import Transaction
from account.factories import CustomerFactory, TransactionFactory
from rest_framework.test import APIClient


class TestCustomerCurrentAmount(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.customer.user)

    def test_transactions(self):
        expected_amount = 0
        for _ in range(0, 10):
            transaction = TransactionFactory(customer=self.customer)
            if transaction.type == Transaction.Type.INCOME:
                expected_amount += transaction.amount
            else:
                expected_amount -= transaction.amount

        self.customer.refresh_from_db()
        self.assertEqual(self.customer.current_amount, expected_amount)
