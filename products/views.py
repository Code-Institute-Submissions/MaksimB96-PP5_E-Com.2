from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """View that renders all Products, and handles sorting/searching"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """View that renders selected Product"""

    product = get_object_or_404(product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
