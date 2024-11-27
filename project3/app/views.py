from django.shortcuts import render,redirect

# Create your views here.
admin_usname='admin'
admin_psword='admin123'
user=[]
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user.append([name,email,username,password])
        print(user)
    return render(request,'index.html')
def index2(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['psword']
        for i in user:
            if username==i[2] and password==i[3]:
                print([i[0]])
                return redirect(home)
    return render(request,'index2.html')
def home(request):
    return render(request,'home.html')
def adminlogin(request):
    if request.method=='POST':
        admin_usname=request.POST['usname']
        admin_pswod=request.POST['psword']
        if admin_usname==admin_usname and admin_pswod==admin_pswod:
            return redirect(adminhome)
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html',{'users':user})
    
                
        