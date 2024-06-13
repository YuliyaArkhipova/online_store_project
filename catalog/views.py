from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def product_list(request):
    products = Product.objects.all()
    context = {"object_list": products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)


def contacts(request):
    return render(request, "contacts.html")



