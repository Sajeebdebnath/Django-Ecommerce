from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import customer
from .models.orders import Order


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','description','image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class CustomerInfo(admin.ModelAdmin):
    list_display = ['full_name','phone','address','email']

class OrderInfo(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'address', 'phone', 'date','status']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(customer,CustomerInfo)
admin.site.register(Order,OrderInfo)