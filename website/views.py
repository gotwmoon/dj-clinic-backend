from django.shortcuts import render

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')    


def contact_view(request):
    return render(request, 'website/contact.html')    

def department_view(request):
    return render(request, 'website/department.html')        

def department_single_view(request):
    return render(request, 'website/department-single.html')            