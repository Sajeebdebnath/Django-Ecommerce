from django.shortcuts import render
from django.views import View
from store.models.product import Product
from store.models.customer import customer

class Cart(View):
    def get(self,request):
        ids = request.session.get('cart').keys()
        products = Product.get_many_product_byID(ids)

        customer_id = request.session.get('customer')
        customers = customer.get_customer_byID(customer_id)
        data = {}
        data['username'] = customers
        data['products'] = products
        return render(request, 'cart.html', data)

