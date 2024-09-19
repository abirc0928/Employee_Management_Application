from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='login_view')
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_from = form.save(commit=False)
            employee_from.user = request.user
            employee_from.save()
            return redirect("homepage")
    else:
        form = EmployeeForm()
    context = {
        "form": form
    }
    return render(request, "add_employee.html", context)

  
def update_and_delete(request):
    employees = Employee.objects.filter(user=request.user)
    context = {
        "employees" : employees
    }
    return render(request, "update_and_delete.html", context)

def update_employee(request, employee_id):

    try:
        employee = Employee.objects.get(pk = employee_id)
        if request.method == "POST":
            employee_form = EmployeeForm(request.POST, instance=employee)
            if employee_form.is_valid():
                employee_form.save()
                return redirect("update_and_delete")
            else:
                return render(request, "update_employee.html", {"form":employee_form})


        employee_form = EmployeeForm(instance=employee)
        return render(request, "update_employee.html", {"form":employee_form})
       
    except Employee.DoesNotExist:
        return HttpResponse("Task does not exist")
    
def delete_employee(requestm,employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
    except employee.DoesNotExist:
        return HttpResponse("Task does not exist")
    return redirect("update_and_delete")

    
