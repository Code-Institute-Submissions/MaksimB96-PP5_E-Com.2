from django.shortcuts import render


def profile(request):
    """Renders User Profile"""
    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
