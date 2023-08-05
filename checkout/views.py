from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing in bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NRdofFm2KTUNg8UQ3YutejekgE0ZQZJFDC8m2zvQS2DENozMWQR6IAGGK71nmxahHGp1FgavgYGwQScYtrOCSt000pj4bVXcs',
        'client_secret': 'test secret',
    }

    return render(request, template, context)
