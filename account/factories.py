import factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from account.models import Customer, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    user = factory.SubFactory(UserFactory)
    current_amount = 0


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    created = factory.Faker('past_datetime', tzinfo=timezone.get_current_timezone())
    amount = factory.Faker('pyint', min_value=0)
    note = ''
    type = factory.Iterator([x[0] for x in Transaction.Type.choices])
    customer = factory.SubFactory(CustomerFactory)
