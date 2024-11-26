from django.shortcuts import render,redirect

# Create your views here.
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
                
        