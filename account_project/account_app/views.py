from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

from django.contrib import messages

from .models import Items

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        if User.objects.filter(username = username).exists():
            messages.error(request , "Username already Taken !")
            
        else:
            
            user = User.objects.create_user(username = username , password = password)
            user.save
            messages.success(request , "Account created successfully !")
            return redirect("login/")
        
    return render(request , "register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request , username = username , password = password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials !")
            
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def home(request):
    
    items = Items.objects.all()
    
    return render(request,"home.html" , {"items" : items})
    