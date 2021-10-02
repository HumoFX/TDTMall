import uuid as uuid
from django.db import models


# Create your models here.
from account.models import Customer, Investor
from product.models import Product


class InstallmentRate(models.Model):
    """
    Тариф рассрочки
    """
    CURRENCY = (
        (1, "сум"),
    )
    price_max = models.DecimalField(decimal_places=2, max_digits=12)
    price_min = models.DecimalField(decimal_places=2, max_digits=12)
    currency = models.IntegerField(choices=CURRENCY, default=1)
    period = models.PositiveSmallIntegerField(help_text="Кол-во месяцев для рассрочки")
    percentage = models.FloatField(help_text="Процент надбавки")


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    installment_rate = models.ForeignKey(InstallmentRate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Invoice(models.Model):
    CURRENCY = (
        (1, "сум"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sum = models.DecimalField(decimal_places=2, max_digits=12)
    currency = models.IntegerField(choices=CURRENCY, default=1)
    transaction = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateField()
    settled_date = models.DateTimeField()
    is_payed = models.BooleanField(default=False)


class Investment(models.Model):
    CURRENCY = (
        (1, "сум"),
    )
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=18, decimal_places=2)
    currency = models.IntegerField(choices=CURRENCY, default=1)
    transaction = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)