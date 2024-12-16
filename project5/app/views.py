from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *

# Create your views here.
admin_usname='admin'
admin_psword='admin123'
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
        else:
            return redirect(userlogin)
    return render(request,'user/userlogin.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,username=username,email=email,password=password)
        data.save()
        return redirect(userlogin)
    return render(request,'user/register.html')

def userhome(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/userhome.html',{'user':user})
    else:
        return redirect(userlogin)

def logout(requset):
    if '_auth_user_id' in requset.session:
        del requset.session['user']
        return redirect(userlogin)
    else:
        return redirect(userlogin)
def adminlogin(request):
    if request.method=='POST':
        admin_usname=request.POST['usname']
        admin_pswod=request.POST['psword']
        if admin_usname==admin_usname and admin_pswod==admin_pswod:
            return redirect(adminhome)
    return render(request,'admin/adminlogin.html')
def adminhome(request):
    return render(request,'admin/adminhome.html')