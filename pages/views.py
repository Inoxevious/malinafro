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
    # for a in cat:
    #         try: 
    #             if a.id:

    #                 department_ads = DepartmentAdverts.objects.all()
    #                 # print('Ads dept ',department_ads.id, ' ___', department_ads.dep.head.user.username)
    #                 # # prod = Product.objects.get(sub_category)
    #                 # department_ads_dict[department_ads.id] = []
    #                 # department_ads_dict[department_ads.id].append(str(department_ads.dep.head.user.username))                                       
    #                 # dept_id_dict[department_ads.id] = []
    #                 # dept_id_dict[department_ads.id].append(str(department_ads.dep.id))
    #                 # product_name_dict[department_ads.id] = []
    #                 # product_name_dict[department_ads.id].append(str(department_ads.product.name))
    #                 # product_price_dict[department_ads.id] = []
    #                 # product_price_dict[department_ads.id].append(str(department_ads.product.price))
    #                 # product_description_dict[department_ads.id] = []
    #                 # product_description_dict[department_ads.id].append(str(department_ads.product.short_description))
    #                 # product_id_dict[department_ads.id] = []
    #                 # product_id_dict[department_ads.id].append(str(department_ads.product.id))
    #                 # product_image_dict[department_ads.id] = []
    #                 # product_image_dict[department_ads.id].append(str(department_ads.product.image))
    #             else:
    #                 department_ads = DepartmentAdverts.objects.all()

    #         except (TypeError, ValueError, OverflowError, Department.DoesNotExist):
    #                 dcost = 'Risk not added yet'
    
    sub_category = SubCategory.objects.all()
    # for sub_category in sub_category:
    #     try:
    #         product  = Product.objects.get(sub_category_id = sub_category.id)
    #         dept_id_dict[sub_category.id] = []
    #         dept_id_dict[department_ads.id].append(str(department_ads.dep.id))   

    #     except (TypeError, ValueError, OverflowError, Product.DoesNotExist):
    #                 dcost = 'Risk not added yet'
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
    print('ARTICLESSSS image', articles)
    context = { 'object_list': paged_object_list,
            
                'about_us': about_us,
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
                'department_ads': department_ads,
    

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

def view_cat_products(request, cat_id):
    print('Cat ID', cat_id)
    cat_products = Product.objects.filter(category_id=cat_id)
    print('CAT PRODCUTS', cat_products)
    depts = Category.objects.all()  
    # print('CATEGORIES', depts.id, "name", depts.short_name)
    context = { 
                'depts': depts,
                'cat_products': cat_products,
    
     }

    return render(request, 'pages/fashe/components/categories_pages/product.html', context)

    
def faq(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/faq.html', context)