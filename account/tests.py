import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from account.models import Transaction, Customer
from account.factories import CustomerFactory, TransactionFactory


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


class TestTransactionAPI(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.customer.user)

    def test_create_transaction_api(self):
        data = {
            'created': datetime.datetime.now(),
            'amount': 1000,
            'note': 'test note',
            'type': Transaction.Type.INCOME,
            'customer': self.customer.id
        }
        response = self.client.post(reverse('transaction-list'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Customer.objects.all().count(), 1)
        self.assertEqual(Transaction.objects.filter(customer=self.customer).count(), 1)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.current_amount, 1000)
