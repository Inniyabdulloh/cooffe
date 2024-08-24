from django.shortcuts import render, redirect
from django.views import View
from .models import CoffeeOffer, CustomersReview, Contact
# Create your views here.

class HomeView(View):
    def get(self, request):
        customer_reviews = CustomersReview.objects.all()
        coffee_types1 = CoffeeOffer.objects.all()[0:4]
        coffee_types2 = CoffeeOffer.objects.all()[4:8]
        context = {'coffee_types1': coffee_types1,
                   'coffee_types2': coffee_types2,
                   'customer_reviews': customer_reviews}
        return render(request, 'index.html', context)





class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        return redirect('main:index')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class CoffeeView(View):
    def get(self, request):
        coffee_types1 = CoffeeOffer.objects.all()[0:4]
        coffee_types2 = CoffeeOffer.objects.all()[4:8]
        context = {'coffee_types1': coffee_types1,
                   'coffee_types2': coffee_types2,
                   }
        return render(request, 'coffee.html', context)
