from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages


def index(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')

        else:
            messages.error(request, 'Invalid username/password!')
            return redirect('/')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['Username']
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        email = request.POST['Email']
        password = request.POST['Password']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print("USER CREATED")
        return redirect('/')
    else:
        return render(request, 'register.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def adminpanel(request):
    user=User.objects.all()
    return render(request,'adminpanel.html', {'info': user})