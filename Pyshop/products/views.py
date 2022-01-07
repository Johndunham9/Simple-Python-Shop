from django.http import HttpResponse, Http404
from .models import Product
from django.shortcuts import render


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'product': product})





