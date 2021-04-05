from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}"

    def re_calculate_current_amount(self):
        self.current_amount = 0
        for t in self.transaction_set.all():
            if t.type == Transaction.Type.INCOME:
                self.current_amount += t.amount
            else:
                self.current_amount -= t.amount
        self.save()


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.customer.re_calculate_current_amount()
