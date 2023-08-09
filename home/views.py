from django.shortcuts import render
from products.models import Product


def index(request):
    """Main index page render"""
 
    products = Product.objects.filter(category__name='honey')
    context = {
        'products': products
    }
    
    return render(request, 'home/index.html', context)
