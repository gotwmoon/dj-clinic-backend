from django.shortcuts import render, get_object_or_404
from .models import Department, Service, TimeSchedule


def index_view(request):
    
    time_schedule = TimeSchedule.objects.all()
    context = {'time_schedule':time_schedule}
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')    


def contact_view(request):
    return render(request, 'website/contact.html')    

def department_view(request):
    deparments = Department.objects.all()
    context = {'deparments':deparments}
    return render(request, 'website/department.html', context)        

def department_single_view(request, pid):

    department = get_object_or_404(Department, id=pid)
    services = department.service_set.all()

    time_schedule = TimeSchedule.objects.all()

    context = {'department': department, 'services':services, 'time_schedule':time_schedule}
    return render(request, 'website/department-single.html', context)       
