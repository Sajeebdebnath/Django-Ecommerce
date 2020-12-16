from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import customer
from django.views import View


class Signup(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        postData = request.POST

        full_name = postData.get('full_name')
        address = postData.get('address')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Draf Data
        fill_data = {
            'full_name': full_name,
            'address': address,
            'phone': phone,
            'email': email
        }
        # Creating object
        oCustomer = customer(full_name=full_name,
                             address=address,
                             phone=phone,
                             email=email,
                             password=password
                             )

        error_message = None
        error_message = self.signup_Validation(oCustomer)

        # Save information

        if (not error_message):
            oCustomer.password = make_password(oCustomer.password)
            oCustomer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': fill_data
            }
            return render(request, 'signup.html', data)

    def signup_Validation(self,oCustomer):
        error_message = None
        if (not oCustomer.full_name):
            error_message = "Name is required !"
        elif (len(oCustomer.full_name) < 4):
            error_message = "Name must be at least 4 character. "
        elif (not oCustomer.address):
            error_message = "Address is required !"
        elif (not oCustomer.phone):
            error_message = "Phone is required !"
        elif (not oCustomer.email):
            error_message = "Email address is required !"
        elif (len(oCustomer.password) < 6):
            error_message = "Password must be at least 6 character. !"
        elif oCustomer.isExits():
            error_message = "This Email already registerd !"
        return error_message