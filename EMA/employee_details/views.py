from django.shortcuts import render
from add_employee. models import Employee
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_view')
# Create your views here.
def employee_details(request, employee_id):
    employee = Employee.objects.get(pk = employee_id)
    context = {
        "employee": employee
    }
    return render(request, "employee_details.html", context)