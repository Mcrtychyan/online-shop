from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def cart_detail(request):
    return render(request, 'cart/detail.html', {'cart_count': 0})

@require_POST
def cart_add(request, product_id):
    return JsonResponse({'count': 1})
