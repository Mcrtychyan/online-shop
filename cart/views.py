from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from myapp.models import Products


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    print(f"DEBUG: {product_id} добавлен, всего: {cart.count()}")
    return JsonResponse({'count': cart.count()})
