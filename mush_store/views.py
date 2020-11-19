from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings
import os
import mimetypes
from cart.cart import Cart
# Create your views here.
from django.views import generic
from ecommerce_app.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("mush_store:cart_detail")

def check_out(request):

    return redirect("mush_store:cart_detail")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("mush_store:cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("mush_store:cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("mush_store:cart_detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("mush_store:cart_detail")


# @login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'pages/fashe/components/cart/cart_detail.html')

def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product':product,
    }
    return render(request, 'pages/fashe/components/product_detail/index.html', context)

def product_category(request, id):
    products = Product.objects.filter(category=id)
    context = {
        'products':products,
    }
    return render(request, 'pages/malin/components/product/product_detail.html', context)