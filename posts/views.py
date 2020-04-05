from django.shortcuts import render , redirect
from .models import MenuItem , NewsLetter
from django.views import View
from . import views
from django.views.generic import TemplateView
from .forms import MenuLoad
from django.http import Http404, HttpResponse, JsonResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def index(request):
    titlex = MenuItem.objects.get(item_id=3)
    titley = MenuItem.objects.get(item_id=6)
    titlez = MenuItem.objects.get(item_id=12)
    context={'titlex':titlex,'titley':titley,'titlez':titlez}
    return render(request,'posts/index.html',context)


class MenuView(TemplateView):
    template_name='posts/menu.html'

    def get(self, request):
        form = MenuLoad(request.GET)
        menu=None
        if form.is_valid():
            search_query=form.cleaned_data['item_category']
            menu = MenuItem.objects.filter(item_category__icontains=search_query)
        p_cake = MenuItem.objects.filter(item_category__icontains='PANCAKE')[:4]
        tea = MenuItem.objects.filter(item_category__icontains='TEA')[:4]
        frap = MenuItem.objects.filter(item_category__icontains='FRAPPE')[:4]
        subs = MenuItem.objects.filter(item_category__icontains='SUBS')[:4]
        x1 = MenuItem.objects.filter(item_category__icontains='PANCAKE')
        x2 = MenuItem.objects.filter(item_category__icontains='EGG')
        x3 = MenuItem.objects.filter(item_category__icontains='PANNIS')
        x4 = MenuItem.objects.filter(item_category__icontains='SUBS')
        x5 = MenuItem.objects.filter(item_category__icontains='WRAPS')
        x6 = MenuItem.objects.filter(item_category__icontains='TEA')
        x7 = MenuItem.objects.filter(item_category__icontains='FRAPPE')
        x8 = MenuItem.objects.filter(item_category__icontains='SMOOTHIE')
        x9 = MenuItem.objects.filter(item_category__icontains='GLUTENF')
        args={
            'form': form,
            'menu': menu,
            'p_cake':p_cake , 
            'tea':tea ,
            'frap':frap,
            'subs':subs,
            'pcake_menu':x1,
            'egg_menu':x2,
            'pannis_menu':x3,
            'sub_menu':x4,
            'wrap_menu':x5,
            'coffee_menu':x6,
            'frap_menu':x7,
            'smoothie_menu':x8,
            'gluten_free_menu':x9,
             
             }
        
        return render(request,self.template_name,args)


def test(request):
    x1 =MenuItem.objects.filter(item_category__icontains='COFFEE')

    context={
        'p':x1,
    }
    return render(request, 'posts/test.html',context)  



def SignUp(request):
    
        if request.method == 'POST':
                post=NewsLetter()
                post.email_name= request.POST.get('email_name')
                post.email_address= request.POST.get('email_address')
                post.telephone_number=request.POST.get('telephone_number')
                post.home_address=request.POST.get('home_address')
                post.description=request.POST.get('description')
                post.save()
                messages.success(request,'Successful')
                response = redirect('/SignUp')
                return response

        else:
                return render(request,'posts/EmailSignUp.html')