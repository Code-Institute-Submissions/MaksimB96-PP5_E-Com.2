from django.shortcuts import render


def view_bag(request):
    """A view that dis[lays the contents of shopping bag"""

    return render(request, 'bag/bag.html')
