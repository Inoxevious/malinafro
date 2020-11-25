from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from account.models import *
import csv
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify
from ecommerce_app import cart
from ecommerce_app.models import *
def dept_detail(request,dept_id):
        totaldict = {}
        dept = Department.objects.get(id=dept_id)
        context = {
                'dept': dept,
        }
        return render(request, 'pages/dept_detail.html', context )

def notice_detail(request,notice_id):     
        totaldict = {}
        notice = NoticeBoard.objects.get(id=notice_id)
        context = {
                'notice': notice,
        }
        return render(request, 'pages/partials/detail.html', context )


def article_detail(request,article_id):
        totaldict = {}
        articles = Articles.objects.get(id=article_id)
        context = {
                'articles': articles,
        }
        return render(request, 'pages/partials/article_detail.html', context )


class HomePageView(TemplateView):
   
    template_name = 'pages/partials/home.html'

    def get_queryset(self, **kwargs):
        global object_list, paged_object_list
        object_list = AccountUser.objects.all()
        print('objet found',object_list)


        paginator = Paginator(object_list,3)
        page = self.request.GET.get('page')
        paged_object_list = paginator.get_page(page)


        return paged_object_list

def index(request):

    global object_list, paged_object_list
    object_list = Category.objects.all()
    print('objet found',object_list)

    paginator = Paginator(object_list,5)
    page = request.GET.get('page')
    paged_object_list = paginator.get_page(page)
    department_ads_dict = {}
    about_us_dict = {}
    appointment_date_dict = {}
    dept_id_dict = {}

    product_id_dict = {}
    product_name_dict = {}
    product_price_dict = {}
    product_image_dict = {}
    product_description_dict = {}
    product_name_dict = {}
    dept_id_dict = {}
    cat = object_list
    print('HOD FOUND',cat)
    
    sub_category = SubCategory.objects.all()
    department_ads = DepartmentAdverts.objects.all()
    about_us = About_us.objects.all()
    print('about us', about_us)
    notices  = NoticeBoard.objects.all()   
    articles  = Articles.objects.all() 
    sub_summer = Product.objects.filter(category_id = 3)
    hunters = Product.objects.filter(category_id = 3)
    on_sale = Product.objects.filter(category_id = 3)
    open_show = Product.objects.filter(category_id = 3)
    ankara_accesories = Product.objects.filter(category_id = 5)
    ankara_senator_wear = Product.objects.filter(category_id = 4)
    hair_skin_care = Product.objects.filter(category_id = 3)
    home_fragrances = Product.objects.filter(category_id =2)
    body_fragrances = Product.objects.filter(category_id = 1)
    department_ads = DepartmentAdverts.objects.filter(category_id = 1)[:1]
    # size1_ankara_senator_wear = Product.objects.filter(size1_model_image = 1)
    depts = Department.objects.all()  
    all_products = Product.objects.all()
    collection = Collection_Banner.objects.all()[:1]
    casual_collection =  Product.objects.filter(sub_category = 2 )
    quick_rail_collection =  Product.objects.filter(sub_category = 1 )
    print('ARTICLESSSS image', articles)
        

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
    menu_ads = MainMenuAds.objects.all()
    menu_ads_summer_look = MainMenuAds.objects.filter(category='summer_look')[:3]
    menu_ads_lovers_show_off = MainMenuAds.objects.filter(category='lovers_show_off')[:3]
    menu_ads_ambitious_personalities = MainMenuAds.objects.filter(category='ambitious_personalities')[:3]
    menu_ads_ambitious_kidz = MainMenuAds.objects.filter(category='ambitious_kidz')[:3]
    menu_ads_fashion_blog = MainMenuAds.objects.filter(category='fashion_blog')[:3]
    menu_items = MenuItems.objects.all()
    context = { 'object_list': paged_object_list,
            
                'about_us': about_us,
                'menu_items':menu_items,
                'casual_collection':casual_collection,
                'quick_rail_collection':quick_rail_collection,
                'menu_ads':menu_ads,
                'menu_ads_summer_look':menu_ads_summer_look,
                'menu_ads_lovers_show_off':menu_ads_lovers_show_off,
                'menu_ads_ambitious_personalities':menu_ads_ambitious_personalities,
                'menu_ads_ambitious_kidz':menu_ads_ambitious_kidz,
                'menu_ads_fashion_blog':menu_ads_fashion_blog,
                # 'product': product,
                'sub_category': sub_category,
                'ankara_accesories':ankara_accesories,
                'ankara_senator_wear':ankara_senator_wear,
                'hair_skin_care':hair_skin_care ,
                'home_fragrances': home_fragrances,
                'body_fragrances':body_fragrances,
                'sub_summer':sub_summer,
                'hunters': hunters,
                'all_products': all_products,
                'on_sale': on_sale,
                'articles': articles,
                'open_show': open_show,
                'collection':collection,
                'department_ads': department_ads,
                'cart_sum':cart_sum,
                'cart_subtotal':cart_subtotal,
                'cart_items': cart_items,
    

     }
    return render(request, 'pages/fashe/components/home/index.html', context)

def guide(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/guide.html', context)

def contact(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/contact.html', context)


def listing(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/listing.html', context)

# def loginn(request):
#     data = 'hie'
#     context = {'data':data}

#     return render(request, 'pages/login.html', context, context)

def primary(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }

    return render(request, 'pages/primary.html', context)

def view_cat_products(request, category_slug):
    print('Cat name',category_slug)
    cat_products = Product.objects.filter(collecion_category=category_slug)
    print('CAT PRODCUTS', cat_products)
    depts = Category.objects.all()  
    # print('CATEGORIES', depts.id, "name", depts.short_name)
    cart_sum = cart.item_count(request)
    cart_subtotal = cart.subtotal(request)
    print("CRT ITEMS SUM", cart_sum)
    if request.method == 'POST':
        try:
            shipping_cost = request.POST['city']
            request.session['shipping_cost'] = shipping_cost
        except MultiValueDictKeyError:
            shipping_cost = 0
    menu_ads = MainMenuAds.objects.all()
    cart_items = cart.get_all_cart_items(request)
    menu_items = MenuItems.objects.all()
    context = { 
                'depts': depts,
                'menu_items':menu_items,
                'menu_ads':menu_ads,
                'cat_products': cat_products,
                'cart_sum':cart_sum,
                'cart_subtotal':cart_subtotal,
                'cart_items': cart_items,
    
     }

    return render(request, 'pages/fashe/components/categories_pages/product.html', context)

    
def faq(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/faq.html', context)