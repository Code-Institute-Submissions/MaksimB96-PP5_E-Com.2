from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from subscription.models import Subscribers
from subscription.forms import SubscribeForm



def index(request):
    """Main index page render and handles News Letter Subscribers"""
    products = Product.objects.filter(category__name='honey')
    form_sub = SubscribeForm()

    try:
        if request.method == 'POST':
            email = request.POST['email']
            subscribed = Subscribers.objects.values_list('email', flat=True)
            if email in subscribed:
                messages.error(request, 'This email has already subscribed!')
            else:
                form_sub = SubscribeForm(request.POST)
                sub_to_form = form_sub.save(commit=False)
                sub_to_form.email = email
                sub_to_form.save()
                messages.success(request, f'{email} has been added to our news list!')
                return redirect('home')
    except ValueError:
        messages.error(request, "Email not valid!")
        return redirect('home')
            

    context = {
        'products': products,
        'form_sub': form_sub,
    }

    return render(request, 'home/index.html', context)


# def unsub(request):


 