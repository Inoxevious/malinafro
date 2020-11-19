from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from .models import Product, Order, LineItem
from .forms import CartForm, CheckoutForm
from . import cart
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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
    return render(request, 'ecommerce_app/make_payment.html', {'order': order, 'form': form})


def index(request):
    all_products = Product.objects.all()
    return render(request, "pages/fashe/components/home/index.html", {
                                    'all_products': all_products,
                                    })


def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        print(form)

        
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            print('CART ITEMS', request)
            return redirect('ecommerce_app:show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'pages/fashe/components/product_detail/index.html', {
                                            'product': product,
                                            'form': form,
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

    return render(request, 'pages/fashe/components/cart/cart_detail.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            'total':total,
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

            return render(request, 'pages/fashe/components/cart/checkout.html', {
                'form': form,
                'cart_items': cart_items,
                'cart_subtotal': cart_subtotal,
                'total':total,
                })


    else:
        form = CheckoutForm()
        cart_items = cart.get_all_cart_items(request)
        print('FOUND CHECKOUT CART ITEMS', cart_items)
        cart_subtotal = cart.subtotal(request)
        shipping_cost = request.session['shipping_cost']

        total = cart_subtotal + Decimal(shipping_cost)
        
        return render(request, 'pages/fashe/components/cart/checkout.html', {
            'form': form,
            'cart_items': cart_items,
            'cart_subtotal': cart_subtotal,
            'total':total,
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
    return render(request, 'pages/fashe/components/cart/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total':total,
        })

@csrf_exempt
def payment_done(request):
    return render(request, 'ecommerce_app/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce_app/payment_canceled.html')