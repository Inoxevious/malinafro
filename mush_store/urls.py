from django.conf.urls import url
from django.urls import path, include
from mush_store import views
app_name = 'mush_store'

# Be careful setting the name to just /blog use userblog instead!
urlpatterns=[
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'), 
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/check_out/',views.check_out,name='check_out'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
   
]