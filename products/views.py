from django.shortcuts import render
from .models import Product


def all_products(request):
    """View that renders all Products, and handles sorting/searching"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
