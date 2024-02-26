from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['__str__']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price','description','Brand','category','product_image']

    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['__str__']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['__str__']

    

