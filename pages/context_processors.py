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
from ecommerce_app.models import *
import csv
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify
from ecommerce_app import cart

def logo_to_context(request):
    global object_list, paged_object_list
    object_list = Category.objects.all()
    print('objet found',object_list)

    paginator = Paginator(object_list,5)
    page = request.GET.get('page')
    paged_object_list = paginator.get_page(page)
    about_us = About_us.objects.all()


    return {
        'object_list': paged_object_list,
        'about_us': about_us,
    }