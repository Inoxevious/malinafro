from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from .models import Product, Order, LineItem
from .forms import CartForm, CheckoutForm
from . import cart
from .models import  *
from paynow import Paynow
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import datetime
import emoji
import random
import json
import time
# Create your views here.

def process_payment_payow(request):
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    paynow = Paynow(
    '9437',
	'5f8250e8-1c59-4d2c-ba00-8bd74693e6c2',
    'http://example.com/gateways/paynow/update', 
    'http://example.com/return?gateway=paynow'
    )
    
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    print("CRT ITEMS", order)
    
    payment = paynow.create_payment(order.id, order.email)
    payment.add('Order {}'.format(order.id),'%.2f' % order.total_cost())
    print('PAYMENT PAYNOW', payment)

    if request.method == 'POST':
        phone = request.POST['phone']
        print('PHONE', phone)
        response = paynow.send_mobile(payment, phone, 'ecocash')
    else:
        response = paynow.send(payment)


    if(response.success):
        poll_url = response.poll_url

        print("Poll Url: ", poll_url)

        status = paynow.check_transaction_status(poll_url)

        time.sleep(30)

        print("Payment Status: ", status.status)
        if status.paid :
            order.paid = True
            order.save()
            
        else :
            return render(request, 'ecommerce_app/make_payment.html', {
                    'order': order,'menu_items':menu_items,
                    'menu_ads':menu_ads, })
    return render(request, 'ecommerce_app/make_payment.html', {
                'order': order,
                'phone':phone,
                'menu_items':menu_items,
                'menu_ads':menu_ads,
                 })

def process_payment(request):

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost(),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('ecommerce_app:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('ecommerce_app:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'ecommerce_app/make_payment.html', {'order': order, 'form': form,                'cart_sum':cart_sum,
                'cart_subtotal':cart_subtotal,
                'cart_items': cart_items,
                'menu_items':menu_items,
                'menu_ads':menu_ads,
                'menu_items':menu_items,
                'menu_ads':menu_ads,
                })


def index(request):
    all_products = Product.objects.all()
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, "pages/fashe/components/home/index.html", {
                                    'all_products': all_products,
                                    'menu_items':menu_items,
                                    'menu_ads':menu_ads,
                                    })


def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        size = request.POST['size']
        color = request.POST['color']
        # product_id = request.form_data['product_id']
        # quantity = request.form_data['quantity']
        print('SIZE...', size)
        print('color...', color)
        # print('product_id...', product_id)
        # print('quantity...', quantity)
        form = CartForm(request, request.POST)
        print(form)

        
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            print('CART ITEMS', request)
            return redirect('ecommerce_app:show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0
    colors = ProductMaterialMainColor.objects.all()
    print('FOUND COLORS', colors)
 
        
    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'pages/fashe/components/product_detail/index.html', {
                                            'product': product,
                                            'form': form,
                                            'cart_sum':cart_sum,
                                            'cart_subtotal':cart_subtotal,
                                            'cart_items': cart_items,
                                            'colors':colors,
                                            'menu_items':menu_items,
                                            'menu_ads':menu_ads,
                                            })
def add_item_to_cart(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        print(form)

        
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            print('CART ITEMS', request)
            return redirect('pages:index')

    form = CartForm(request, initial={'product_id': product.id})
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)

        
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'pages/fashe/components/product_detail/index.html', {
                                            'product': product,
                                            'form': form,
                                            'cart_sum':cart_sum,
                                            'cart_subtotal':cart_subtotal,
                                            'cart_items': cart_items, 
                                            'menu_items':menu_items,
                                            'menu_ads':menu_ads,  
                                                                                    
                                            })

def show_cart(request):
    shipping_cost = 0

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    
    print('FOUND CART ITEMS', cart_items)
    cart_subtotal = cart.subtotal(request)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    
    total = cart_subtotal + Decimal(shipping_cost)
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'pages/fashe/components/cart/cart_detail.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            'total':total,
                                            'cart_sum':cart_sum,
                                            'cart_subtotal':cart_subtotal,
                                            'cart_items': cart_items,
                                            'menu_items':menu_items,
                                            'menu_ads':menu_ads,                                            
                                            })


def checkout(request):
    print('GOOD MORNING')
    if request.method == 'POST':
        print('GOOD MORNING')
        form = CheckoutForm(request.POST)
        print('FORM DATAA',form)
        if form.is_valid():
            print('GOOD MORNING VL')
            cleaned_data = form.cleaned_data
            uname = cleaned_data.get('name')
            print('username',uname)
            shipping_cost = request.session['shipping_cost']

            o = Order(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
                address = cleaned_data.get('address'),
                phone = cleaned_data.get('phone'),
                city = cleaned_data.get('city'),
                shippig_cost = shipping_cost,
            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            cart_subtotal = cart.subtotal(request)
            shipping_cost = request.session['shipping_cost']
            total = cart_subtotal + Decimal(shipping_cost)
            print('oRDER TOTAL', total)
            request.session['order_total'] = str(total)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    size= cart_item.size,
                    color= cart_item.color,
                    order_id = o.id
                )

                li.save()

            cart.clear(request)
            request.session['order_id'] = o.id
            return redirect('ecommerce_app:process_payment')


            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('ecommerce_app:checkout')
        else:
            cart_items = cart.get_all_cart_items(request)
            print('FOUND CHECKOUT CART INV ITEMS', cart_items)
            cart_subtotal = cart.subtotal(request)
            shipping_cost = request.session['shipping_cost']


        
            total = cart_subtotal + Decimal(shipping_cost)
            cart_sum = cart.item_count(request)
            cart_subtotal = cart.subtotal(request)
            print("CRT ITEMS SUM", cart_sum)
            if request.method == 'POST':
                try:
                    shipping_cost = request.POST['city']
                    request.session['shipping_cost'] = shipping_cost
                except MultiValueDictKeyError:
                    shipping_cost = 0

            cart_items = cart.get_all_cart_items(request)
            menu_items = MenuItems.objects.all()
            menu_ads = MainMenuAds.objects.all()
            return render(request, 'pages/fashe/components/cart/checkout.html', {
                'form': form,
                'cart_items': cart_items,
                'cart_subtotal': cart_subtotal,
                'total':total,
                'cart_sum':cart_sum,
                'cart_items': cart_items,
                'menu_items':menu_items,
                'menu_ads':menu_ads,
                })


    else:
        form = CheckoutForm()
        cart_items = cart.get_all_cart_items(request)
        print('FOUND CHECKOUT CART ITEMS', cart_items)
        cart_subtotal = cart.subtotal(request)
        shipping_cost = request.session['shipping_cost']

        total = cart_subtotal + Decimal(shipping_cost)
        cart_sum = cart.item_count(request)
        cart_subtotal = cart.subtotal(request)
        print("CRT ITEMS SUM", cart_sum)
        if request.method == 'POST':
            try:
                shipping_cost = request.POST['city']
                request.session['shipping_cost'] = shipping_cost
            except MultiValueDictKeyError:
                shipping_cost = 0

        cart_items = cart.get_all_cart_items(request)
        menu_items = MenuItems.objects.all()
        menu_ads = MainMenuAds.objects.all()      
        return render(request, 'pages/fashe/components/cart/checkout.html', {
            'form': form,
            'cart_items': cart_items,
            'cart_subtotal': cart_subtotal,
            'total':total,
            'cart_sum':cart_sum,
            'cart_items': cart_items,
            'menu_items':menu_items,
            'menu_ads':menu_ads,
            })



def request_to_order(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.requested = True
    order.save()
    
    form = CheckoutForm()
    cart_items = cart.get_all_cart_items(request)


    total = request.session['order_total']
    messages.add_message(request, messages.INFO, 'Order number: {} for {}  of ${} is Successfully  Placed!'.format(order.id, order.name, total))
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'pages/fashe/components/cart/checkout.html', {
        'form': form,
        'cart_sum':cart_sum,
        'cart_subtotal':cart_subtotal,
        'cart_items': cart_items,
        'menu_items':menu_items,
        'menu_ads':menu_ads,
        })

@csrf_exempt
def payment_done(request):
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'ecommerce_app/payment_done.html', {
                                            'cart_sum':cart_sum,
                                            'cart_subtotal':cart_subtotal,
                                            'cart_items': cart_items,
                                            'menu_items':menu_items,
                                            'menu_ads':menu_ads,
    })


@csrf_exempt
def payment_canceled(request):
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0

    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    menu_ads = MainMenuAds.objects.all()
    return render(request, 'ecommerce_app/payment_canceled.html',{
                                            'cart_sum':cart_sum,
                                            'menu_items':menu_items,
                                            'menu_ads':menu_ads,
                                            'cart_subtotal':cart_subtotal,
                                            'cart_items': cart_items,
    })