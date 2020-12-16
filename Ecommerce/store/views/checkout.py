from django.shortcuts import redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.orders import customer

class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customers = request.session.get('customer')
        cart = request.session.get('cart')
        products = list(Product.get_many_product_byID(cart.keys()))

        for product in products:
            order = Order(customer=customer(id=customers),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart']={}

        return redirect('/cart')



