import uuid as uuid
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

User = get_user_model()


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    def __str__(self):
        return self.name


class Product(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = RichTextField()
    characteristic = RichTextField()
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    is_active = models.BooleanField(default=False, verbose_name='активный')


class ProductAttachments(Base):
    def product_attachment_path(instance, filename):
        return "product/{0}/{1}".format(instance.product.id, filename)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to=product_attachment_path)
    is_active = models.BooleanField(default=False, verbose_name='активный')


class ProductPrice(Base):
    price = models.DecimalField(decimal_places=2, max_digits=12)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name='активный')


class ProductDiscount(Base):
    discount = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    product_price = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
