from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password = request.POST['cpassword']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username not available")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password)
                user.save();
                return redirect('login')


        else:

            messages.info(request,"Password not matched")
            return redirect('register')

        return redirect('/')

    return render(request, "register.html")


def new(request):
    if request.method == 'POST':
        return redirect('details')
    return render(request, "new.html")

def details(request):
    if request.method == 'POST':
        return redirect('/')
    return render(request,"details.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
    return render(request,"logout.html")