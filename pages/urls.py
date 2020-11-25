from django.conf.urls import url
from django.urls import path, include
from .views import *
# SET THE NAMESPACE!
app_name = 'pages'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('home', HomePageView.as_view(), name='home'),
    path('index/', index, name='index'),
    path('<int:notice_id>/notice_detail/', notice_detail, name='notice_detail'),
    path('<int:article_id>/article_detail/', article_detail, name='article_detail'),
    path('<int:dept_id>/dept_detail/', dept_detail, name='dept_detail'),
    path('view_cat_products/<slug:category_slug>/',
        view_cat_products, name='view_cat_products'),
    path('faq/', faq, name='faq'),
   
]