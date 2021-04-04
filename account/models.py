from django.db import models


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = 'INCOME', 'รายรับ'
        EXPENSE = 'EXPENSE', 'รายจ่าย'

    created = models.DateTimeField()
    amount = models.IntegerField()
    note = models.TextField()
    type = models.CharField(max_length=32, choices=Type.choices)

    def __str__(self):
        return f"{self.type} [{self.amount}]"
