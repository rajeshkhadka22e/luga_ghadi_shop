from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(
            username=email,  # Using email as the username
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Authenticate and log in the user
        login(request, user)

        # Retrieve full name using `get_full_name()`
        full_name = user.get_full_name()
        messages.success(request, f"Welcome, {full_name}!")

        # Redirect to a success page or dashboard
        return redirect('home')

    return render(request, 'register_account.html')
