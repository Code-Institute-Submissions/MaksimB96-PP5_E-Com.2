from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django_pandas.io import read_frame

from .forms import SubscriberAdminNews
from .models import Subscribers


def admin_news_form(request):
    """Handles The admin news section and sends mail"""

    email_subs = Subscribers.objects.all()
    data_frame = read_frame(email_subs, fieldnames=['email'])
    mail_list = data_frame['email'].values.tolist()

    if request.method == 'POST':
        forms = SubscriberAdminNews(request.POST)
        if forms.is_valid():
            forms.save()
            title = forms.cleaned_data.get('title')
            news_body = forms.cleaned_data.get('news_body')
            send_mail(
                title,
                news_body,
                settings.DEFAULT_FROM_EMAIL,
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'News Article has been \
            sent to all subscribers!')
            return redirect('admin_news')
    else:
        forms = SubscriberAdminNews()

    context = {
        'forms': forms,
    }
    return render(request, 'subscription/newsletter.html', context)


def unsubscribe(request):

    try:
        subscribed = Subscribers.objects.values_list('email', flat=True)
        if request.method == 'POST':
            email = request.POST['email']

            if email in subscribed:
                remove_sub = Subscribers.objects.get(email=email)
                remove_sub.delete()
                messages.success(request, f'{email}, has\
                 been successfully removed!')
            else:
                messages.error(request, 'Sorry,\
                 this email is not previously subscribed!')

            return redirect('home')

    except Exception:
        messages.error(request, 'There \
        seems to be a problem! Please try again later!')
        return redirect('home')

    return render(request, 'subscription/unsubscribe.html')
