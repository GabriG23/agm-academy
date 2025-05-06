from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    '''
    questa vista recupera tutti i prodotti dal databse e li passa al template HTML product_list.html
    '''
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})