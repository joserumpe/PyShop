from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OffersAdmin)
admin.site.register(Product, ProductAdmin)
