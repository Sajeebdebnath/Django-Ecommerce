from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from store.models.customer import customer

# Create your views here.

class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = None
        category = Category.Get_all_Catogreis()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.Get_all_products_by_id(categoryID)
        else:
            product = Product.Get_all_products()

        customer_id = request.session.get('customer')
        customers = customer.get_customer_byID(customer_id)

        data = {}
        data['username'] = customers
        data['products'] = product
        data['category'] = category
        print('you are', request.session.get('email'))
        print('customer',customers)
        return render(request, 'index.html', data)

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('Your cart',request.session['cart'])
        return redirect('homepage')


