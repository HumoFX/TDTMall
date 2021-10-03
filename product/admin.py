from django.contrib import admin
from product.models import *


# Register your models here.
class ProductAttachmentInline(admin.TabularInline):
    extra = 1
    model = ProductAttachments


class ProductPriceInline(admin.TabularInline):
    extra = 1
    model = ProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', ]
    inlines = [ProductAttachmentInline, ProductPriceInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice)
admin.site.register(ProductDiscount)
admin.site.register(ProductAttachments)
