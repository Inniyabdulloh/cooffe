from django.urls import path
from .views import HomeView, ContactView, AboutView, CoffeeView
app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('coffee/', CoffeeView.as_view(), name='coffee'),
]