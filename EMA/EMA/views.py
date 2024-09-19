from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from add_employee.models import Employee

@login_required(login_url="login_view")
def home(request):
    query = request.GET.get("q", None)
    employees = Employee.objects.all()   # Get the search term from the query parameter
    query = request.GET.get('q') 
    if query:
        employees = employees.filter(name__icontains=query) |\
                    employees.filter(designation__icontains=query) |\
                    employees.filter(short_description__icontains=query) |\
                    employees.filter(user__first_name__icontains=query) 

    context = {"employees": employees}
    return render(request, "home.html", context)
