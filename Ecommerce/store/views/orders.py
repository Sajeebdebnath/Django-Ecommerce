from django.shortcuts import render
from django.views import View
from store.models.orders import Order
from store.models.customer import customer

class OrderDetails(View):
    def get(self,request):
        customers = request.session.get('customer')
        orders = Order.get_orders_byID(customers)

        customer_id = request.session.get('customer')
        customers = customer.get_customer_byID(customer_id)
        data = {}
        data['username'] = customers
        data['orders'] = orders
        return render(request, 'orders.html',data)


