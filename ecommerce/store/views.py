from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cart(request):
    cart_items = []  # oppure prendi i dati reali dal modello/sessione
    cart_total = 0
    return render(request, 'cart.html', {'cart': cart_items, 'cart_total': cart_total})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})