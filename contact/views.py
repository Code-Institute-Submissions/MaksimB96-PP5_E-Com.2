from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import ContactForm
from .forms import ContactFormPage
from subscription.forms import SubscribeForm

# Create your views here.


def contact_us(request):
    contact_form = ContactFormPage()
    form_sub = SubscribeForm()
    try:
        if request.method == 'POST':
            contact_form = ContactFormPage(request.POST)

            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Thank\
                 you for getting in contact with us!')
                return redirect('home')
            else:
                messages.error(request, 'Whoops!\
                 There seems to be an error with your form!')

    except ValueError:
        messages.error(request, 'Please\
         make sure all fields are filled in!')

    context = {
        'contact_form': contact_form,
        'form_sub': form_sub,
    }

    return render(request, 'contact/contact_us.html', context)
