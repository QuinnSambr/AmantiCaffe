from csv import writer

import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, send_mail
from django.core.validators import validate_email
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from . import views
from .models import *


# Create your views here.

def index(request):
    return render(request,'posts/index.html')


def Menu(request):
    data_dict = {
        'p': 'PANCAKE',
        'e': 'EGG',
        'pn': 'PANNIS',
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

    return render(request, 'posts/Menu.html', context)



def SignUp(request):

        if request.method == 'POST':
                post=NewsLetter()
                try: 
                    validate_email(request.POST.get('email_address'))
                except ValidationError:
                    messages.error(request,'Please Enter Valid Information.')
                    response = redirect('/SignUp#Redirected')
                    return response
                else:
                    post.email_name= request.POST.get('email_name')
                    post.email_address= request.POST.get('email_address')
                    post.telephone_number=request.POST.get('telephone_number')
                    post.home_address=request.POST.get('home_address')
                    post.description=request.POST.get('description')
                    post.save()
                    welcome_msg='''
                    Hey %s,
                    I’m Victoria Rattansingh, the founder of Amanti Del Caffe and I’d like to personally thank you for signing up to our NewsLetters.We established Amanti Del Caffe in order to provide you with the best variaty of Coffee and Food Items Imaginable.
                    I’d love to hear what you think about our selection and if there is anything we can improve. If you have any questions, please reply to this email. I’m always happy to help!
                    V. Rattansingh
                    :)

                    '''%(request.POST.get('email_name'))
                    send_mail(
                        'Amanti Del Caffe',
                        welcome_msg,
                        'notquinn223@gmail.com',
                        [request.POST.get('email_address')],
                        fail_silently=False,
                            )
                    messages.success(request,'Successfully Signed Up For NewsLetter.')
                    response = redirect('/SignUp#Redirected')
                    return response

        else:
                return render(request,'posts/EmailSignUp.html')



def Order(request):
    Listx=''
    if request.method == 'POST':
        url =request.POST.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for x in soup.find_all('iframe'):
            Listx=x.get('src')

    context={
        'x':Listx,
        }
    print(Listx)

    return render(request,'posts/Order.html',context)
