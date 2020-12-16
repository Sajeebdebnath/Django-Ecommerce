from django.shortcuts import render
from django.views import View
from store.models.customer import customer

class CustomerInfo(View):
    def get(self,request):
        customer_id = request.session.get('customer')
        customers = customer.get_customer_byID(customer_id)
        data = {}
        data['username'] = customers
        return render(request, 'customer.html',data)