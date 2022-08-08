
import email
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AppoinmentForm, CustomUserCreationForm, PatientForm
from .models import Appoinment, Patient
from website.models import Department
from django.core.mail import send_mail

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

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect('/')

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


@login_required(login_url='login')
def appionment(request):

    patient = request.user.patient
    departments = Department.objects.all()

    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            
            patient_obj = form.save(commit=False)
            patient_obj.patient = patient

            clean_data = form.cleaned_data
            subject = 'Appointment Request'
            msg= "Name: "  + clean_data['name'] + ", Email: " + clean_data['email'] + ", Date: " + str(clean_data['date']) + ", Message: " + clean_data['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [clean_data['email']]
            send_mail(subject, msg, email_from, recipient_list)

            patient_obj.save()
            return redirect('confirmation')
        else:
            messages.error(request, "An error has accurrede during appoinment!")

    form = AppoinmentForm()
    context = {'form':form, 'departments':departments, 'patient':patient}
    return render(request, 'users/appointment.html', context)

def confirmation(request):
    appionments = Appoinment.objects.all()
    return render(request, 'users/confirmation.html', {'appionments':appionments})    

def update_patient_profile(request):
    patient = request.user.patient

    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated")
        else:
            messages.error(request, "An error has accurrede during update profile!")


            
    context = {'form':form}
    return render(request, 'users/patient-profile.html', context)    