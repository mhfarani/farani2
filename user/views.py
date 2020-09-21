from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from store.models import buyproduct
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'your account has been created! you are able now to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})
@login_required
def profile(request):
    context={
        'buyproduct':buyproduct.objects.all()
    }


    return render(request,'user/profile.html',context)

