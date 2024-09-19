from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import user_profile
from .forms import UserProfileForm
@login_required(login_url='login_view')
# Create your views here.
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)
    try:
        # Try to get the user's profile
        user_profile_data = user_profile.objects.get(user=user)
        profile_exists = True  # Flag to check if profile exists
    except user_profile.DoesNotExist:
        # If no profile exists for the user, set profile_data to None
        user_profile_data = None
        profile_exists = False  # Flag to indicate profile does not exist
    
    context = {
        "user_name": user_name,
        "user": user,
        "user_profile_data": user_profile_data,
        "profile_exists": profile_exists  # Pass the flag to the template
    }
    return render(request, "profile.html", context)

def add_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)  # Don't commit yet, as we need to set the user
            user_profile.user = request.user  # Set the logged-in user
            user_profile.save()
            return redirect(reverse("profile", kwargs={"user_name": request.user.username})) # Redirect to the appropriate view after saving
    else:
        form = UserProfileForm()

    context = {
        "form": form
    }
    return render(request, "add_profile.html", context)
    
def update_profile(request, user_id):
    try:
        profile_data = user_profile.objects.get(pk = user_id)
        if request.method == "POST":
            form = UserProfileForm(request.POST, instance=profile_data)
            if form.is_valid():
                form.save()
                return redirect(reverse("profile", kwargs={"user_name": request.user.username}))
            else:
                return render(request, "update_profile.html", {"form":UserProfileForm})

        else:
            form = UserProfileForm(instance=profile_data)
        context = {
            "form":form
        }
        print(profile_data)
        return render(request, "update_profile.html",context)
    except profile_data.DoesNotExist:
        return HttpResponse("Task does not exist")
