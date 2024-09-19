from django.urls import path
from .views import profile, add_profile, update_profile
urlpatterns = [
    path('add/', add_profile, name="add_profile"),
    path('<str:user_name>/', profile, name="profile" ),
    path('update/<int:user_id>/', update_profile, name="update_profile" ),
]
