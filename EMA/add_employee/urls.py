from django.urls import path, include
from .viwes import add_employee,update_employee, update_and_delete,delete_employee
urlpatterns = [
    path('add/', add_employee, name="add_employee"),
    path('update/<int:employee_id>', update_employee, name="update_employee"),
    path('delete/<int:employee_id>', delete_employee, name="delete_employee"),
    path('update_and_delete/', update_and_delete, name="update_and_delete"),
]
