from django.shortcuts import render


def index(request):
    """Main index page render"""
    
    return render(request, 'home/index.html')
