from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}"


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = 'INCOME', 'รายรับ'
        EXPENSE = 'EXPENSE', 'รายจ่าย'

    created = models.DateTimeField()
    amount = models.IntegerField()
    note = models.TextField()
    type = models.CharField(max_length=32, choices=Type.choices)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} [{self.amount}]"
