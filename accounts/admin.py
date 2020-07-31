from django.contrib import admin
from accounts.models import Customer,Orders,Product,Tags
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tags)
admin.site.register(Orders)
