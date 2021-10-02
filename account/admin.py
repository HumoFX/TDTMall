from django.contrib import admin
from account.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Investor)
admin.site.register(CustomerSalary)
admin.site.register(Organization)
