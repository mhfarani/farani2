from django.shortcuts import render
from .models import product,buyproduct
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    context={
        'product':product.objects.all(),
        'user':User.objects.all()
    }
    return render(request, 'store/home.html', context);
def about(request):
    return render(request,'store/about.html',{'title':'about'});

def addbuy(request, pr):
    context = {
        'product': product.objects.all(),
        'user': User.objects.all()
    }
    br = request.user
    x = buyproduct(product=product.objects.get(pk=pr), buyer=br)
    x.save()
    return render(request, 'store/home.html', context);