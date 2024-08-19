from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout


def login(request):
    error_msg=None
    user = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            auth_login(request,user)
            return redirect("list")
        else:
            error_msg = "Invalid username or password"
            
    return render(request, "users/login.html",{'user':user ,'error_msg' :error_msg})

def logout(request):
    auth_logout(request)
    return redirect("login")


def signup(request):
    user = None
    error_msg=None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_msg = str(e)
    
    return render(request, "users/user_create.html",{'user':user ,'error_msg' :error_msg})


                