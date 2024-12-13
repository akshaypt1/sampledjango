from django.shortcuts import render,redirect
from django.contrib.auth.models import user,auth
from .models import *

# Create your views here.
def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        # data=user.objects.all()
        # for i in data:
        #     if i.email==email and i.password==password:
        #         print('loggedin')
        #         request.session['userlog']=i.email
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
        else:
            return redirect(userlogin)
    return render(request,'user/userlogin.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # data=user.objects.create(name=name,email=email,password=password)
        data=user.objects.create_user(name=name,email=email,password=password)
        
        data.save()
        return redirect(userlogin)
    return render(request,'user/register.html')

def userhome(request):
    if '_auth_user_id' in request.session:
        user=user.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/userhome.html',{'user':user})
    else:
        return redirect(userlogin)

    # if 'userlog' in request.session:
    #     return render(request,'user/userhome.html')
    # else:
    #     return redirect(userlogin)

def logout(requset):
    if '_auth_user_id' in request.session:
        del requset.session['user']
        return redirect(userlogin)
    else:
        return redirect(userlogin)
    
    
    # if 'userlog' in requset.session:
    #     del requset.session['userlog']
    #     return redirect(userlogin)
    # else:
    #     return redirect(userlogin)