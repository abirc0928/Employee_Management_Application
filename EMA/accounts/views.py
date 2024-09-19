from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            request.session['username'] = user.username
            return redirect("homepage")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context)

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_view")
        
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect("login_view")

