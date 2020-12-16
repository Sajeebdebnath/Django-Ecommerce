from django.db import models

class customer(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=300)


    def register(self):
        self.save()

    def isExits(self):
        if customer.objects.filter(email = self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False
    def __str__(self):
        return self.full_name

    @staticmethod
    def get_customer_byID(customer_id):
        return customer.objects.filter(id=customer_id)