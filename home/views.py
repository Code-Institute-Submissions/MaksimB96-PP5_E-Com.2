from django.shortcuts import render
from django.conf import messages
from django.core.mail import send_mail

from products.models import Product
from subscription.models import Subscribers



def index(request):
    """Main index page render and handles News Letter Subscribers"""
    products = Product.objects.filter(category__name='honey')

    if request.method = 'POST':
        form = SubscriberForm

    context = {
        'products': products
    }

    return render(request, 'home/index.html', context)
