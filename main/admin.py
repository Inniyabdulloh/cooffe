from django.contrib import admin
from .models import CoffeeOffer, CustomersReview, Contact
# Register your models here.

admin.site.register(CoffeeOffer)
admin.site.register(CustomersReview)
admin.site.register(Contact)