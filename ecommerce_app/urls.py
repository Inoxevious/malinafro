from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'ecommerce_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>/',
        views.show_product, name='product_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('request_to_order/', views.request_to_order, name='request_to_order'),
    path('process_payment_payow/', views.process_payment_payow, name='process_payment_payow'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('add_item_to_cart/<int:product_id>/<slug:product_slug>/', 
        views.add_item_to_cart, name='add_item_to_cart'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]