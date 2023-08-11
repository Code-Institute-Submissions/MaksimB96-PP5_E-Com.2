from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import SubscriberAdminNews
from .models import Subscribers


def admin_news_form(request):
    """Handles The admin news section and sends mail"""
    form = SubscriberAdminNews()
    if request.method == 'POST':
        form = SubscriberAdminNews(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'News Article has been sent to all subscribers!')
            return redirect('admin_news')
        else:
            form = SubscriberAdminNews()

    context = {
        'form': form,
    }

    return render(request, 'subscription/newsletter.html', context)

