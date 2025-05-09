from django.shortcuts import render
from .models import Product
import matplotlib.pyplot as plt
import io
import base64

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

def product_price_chart(request):
    products = Product.objects.all()
    names = [p.name for p in products]
    prices = [float(p.price) for p in products]

    # Crea il grafico
    fig, ax = plt.subplots()
    ax.bar(names, prices)
    ax.set_ylabel('Prezzo (€)')
    ax.set_xlabel('Prodotto')
    ax.set_title('Prezzi dei Prodotti')
    plt.xticks(rotation=45, ha='right')

    # Salva il grafico in memoria, invece di salvarlo come immagine
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close(fig)

    return render(request, 'price_chart.html', {'graphic': graphic})
