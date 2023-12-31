from django.shortcuts import (
    render,
    redirect,
    reverse, HttpResponse, get_object_or_404)

from django.contrib import messages

from products.models import Product
from subscription.forms import SubscribeForm


def view_bag(request):
    """A view that dis[lays the contents of shopping bag"""

    form_sub = SubscribeForm()
    context = {
        'form_sub': form_sub,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """Allows for adding items to shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated {size.upper()} { product.name } to \
                    {bag[item_id]["items_by_size"][size]}!')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} { product.name } \
                     to shopping bag!')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} { product.name } \
                to shopping bag!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated { product.name } quantity \
                 to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Added { product.name } to shopping bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Allows for adjusting quantities in the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} { product.name } to \
                 {bag[item_id]["items_by_size"][size]}!')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} { product.name } \
                from shopping bag!')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated { product.name } quantity to \
                 {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed { product.name } from shopping bag!')

    request.session['bag'] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Allows for removing bag items"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} { product.name } \
                from shopping bag!')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed { product.name } from shopping bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing Item! : {e}')
        return HttpResponse(status=500)
