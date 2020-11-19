from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import AccountUser


# Create your views here.
def email_check(user):
    
    return user

# @user_passes_test(email_check)
@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    id = user.id
    dash_id = AccountUser.objects.all()
    for i in dash_id:
        j = i.user_class
        print(j)

    for userclass in dash_id:
        if userclass.user_id == id:
            dash_class = userclass.user_class

    userd_class = dash_class
    data = User.objects.all()

    template = ''
    context = {}

    if userd_class == 'farmer':
        context = 'farmer'
        template = 'farmer_dash.html'

    elif userd_class == 'agent':
        context = 'agent'
        template = 'agent_dash.html'

    elif userd_class == 'investor':
        context = 'investor'
        template = 'investor_dash.html'

    elif userd_class == 'invest manager':
        context = 'im'
        template = 'im_dash.html'
        
    return render(request, template, context)




