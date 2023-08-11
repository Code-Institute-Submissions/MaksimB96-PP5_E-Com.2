from django.shortcuts import render


def admin_news_form(request):
    """Handles The admin news section and sends mail"""
    
    return render(request, 'subscriptions/newsletter.html')

