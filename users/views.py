from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from website.models import Department


def login_view(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)        
        except:
            messages.error(request, "User does not exist")

            user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'users/login-signup.html')                

def logout_view(request):
    pass

def signup_view(request):

    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()

            messages.success(request, "Your account created successfuly")

            login(request, user)
            return redirect('/')

        else:
            messages.error(request, "An error has accurrede during registration!")
    context = {'page':page, 'form':form}
    return render(request, 'users/login-signup.html', context)        

def appiontment(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'users/appointment.html', context)