from django.contrib import admin
from product.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(ProductDiscount)
admin.site.register(ProductAttachments)