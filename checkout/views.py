from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing in bag!")
        return redirect(reverse('products'))

    order_from = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_from,
    }

    return render(request, template, context)
