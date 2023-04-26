from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


# Create your views here.

def logedin(request):
    return render(request, "logedin.html")
def form1(request):
    if request.method == 'POST':
        messages.info(request, "Application Accepted")
    return render(request, "form1.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)  # for login
            return redirect('auth:logedin')  # goes to homepage

        else:
            messages.info(request, "invalid credentials")
            return redirect('auth:login')

    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('auth:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already registered")
                return redirect('auth:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('auth:login')
            messages.info(request, "user created")
            print("user created")
        else:
            messages.info(request, "passwords are not matching")
            return redirect('auth:register')
        return redirect('/')  # homepage
    return render(request, "register.html")
