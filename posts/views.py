from django.shortcuts import render , redirect
from .models import *
from django.views import View
from . import views
from django.http import Http404, HttpResponse, JsonResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.

def index(request):
    return render(request,'posts/index.html')


def Menu(request):
    data_dict = {
        'p': 'PANCAKE',
        'e': 'EGG',
        'pn': 'PANINIS',
        's': 'SUBS',
        'w': 'WRAPS',
        't': 'TEA',
        'f': 'FRAPPE',
        'sm': 'SMOOTHIE',
        'gf': 'GLUTENF',
        'wa': 'WAFFLES',
        'to': 'TOAST',
        'hp': 'HOTPASTA',
        'b': 'BAGELS',
        'fr': 'FRIES',
        'sa': 'SALADS',
        'd': 'DESSERTS',
    }
    context = {}

    for key, value in data_dict.items():
        context[key] = MenuItem.objects.filter(item_category__icontains=value)

    return render(request, 'posts/menu.html', context)


def SignUp(request):

        if request.method == 'POST':
                post=NewsLetter()
                try:
                    validate_email(request.POST.get('email_address'))
                except  ValidationError:
                    messages.error(request,'Information is invalid please re-enter')
                    response = redirect('/SignUp#Redirected')
                    return response
                else:
                    post.email_name= request.POST.get('email_name')
                    post.email_address= request.POST.get('email_address')
                    post.telephone_number=request.POST.get('telephone_number')
                    post.home_address=request.POST.get('home_address')
                    post.description=request.POST.get('description')
                    post.save()
                    messages.success(request,'Successfully Signed Up For NewsLetter')
                    response = redirect('/SignUp#Redirected')
                    return response

        else:
                return render(request,'posts/EmailSignUp.html')

