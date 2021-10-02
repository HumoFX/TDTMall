import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


# REFERENCE CLASSES
class Organization(models.Model):
    TYPE = (
        (1, "ЧП"),
        (2, "ООО")
    )
    name = models.CharField(max_length=100)
    type = models.IntegerField(choices=TYPE, default=1)
    inn = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    checking_account = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


#  USER CLASSES
class User(AbstractUser):
    def user_image_path(instance, filename):
        return 'user/{0}/img/{1}'.format(instance.username, filename)

    phone = models.CharField(max_length=20, null=True, blank=True)
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    image = models.ImageField(upload_to=user_image_path, null=True, blank=True)


class Provider(models.Model):
    TYPE = (
        (1, "физическое лицо"),
        (2, "юридическое лицо")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE, default=1)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=50, null=True, blank=True)


class Customer(models.Model):
    def user_passport_path(instance, filename):
        return 'user/{0}/passport/{1}'.format(instance.user.username, filename)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inn = models.CharField(max_length=50),
    passport = models.FileField(upload_to=user_passport_path)
    is_verified = models.BooleanField(default=False)


class CustomerSalary(models.Model):
    CURRENCY = (
        (1, "сум"),
    )
    date = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=12)
    currency = models.IntegerField(choices=CURRENCY, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Investor(models.Model):
    TYPE = (
        (1, "физическое лицо"),
        (2, "юридическое лицо"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE, default=1)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=50, null=True, blank=True)
