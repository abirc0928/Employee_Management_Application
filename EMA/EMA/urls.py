from django.contrib import admin
from django.urls import path, include
from .views import home
from accounts.views import login_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login_view"),
    path('home/', home, name="homepage"),
    path('employee/', include("add_employee.urls")),
    path('employee_details/', include("employee_details.urls")),
    path('accounts/', include("accounts.urls")),
    path('profile/', include("profile_info.urls")), 
]
