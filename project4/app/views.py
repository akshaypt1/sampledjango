from django.shortcuts import render

# Create your views here.
admin_usname='admin'
admin_psword='admin123'
def userlogin(request):
    return render(request,'user/userlogin.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
    return render(request,'user/register.html')