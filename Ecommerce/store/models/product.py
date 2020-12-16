from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default=' ')
    image = models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_many_product_byID(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def Get_all_products():
        return Product.objects.all().order_by('-id')

    @staticmethod
    def Get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return  Product.Get_all_products()

    def __str__(self):
        return self.name