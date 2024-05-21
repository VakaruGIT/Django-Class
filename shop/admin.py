from django.contrib import admin
from shop.models import Product

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ShopAdmin)
