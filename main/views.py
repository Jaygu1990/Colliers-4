from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def index(request):
    mydict ={'insert_me':'This is main page'}
    return render(request,"main.html",context=mydict)


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('main:main'))
            else:
                return HttpResponse("Ops! Account not active")
        else:
            print("someone tried to login but failed")
            return HttpResponse("Invalid login details")
    else:
        return render(request,'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:main'))

