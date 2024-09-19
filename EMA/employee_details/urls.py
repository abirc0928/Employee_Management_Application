
from django.urls import path, include
from .views import employee_details
urlpatterns = [
    path('<int:employee_id>/', employee_details, name="employee_details")
]