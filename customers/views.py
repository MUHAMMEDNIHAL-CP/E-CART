from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Customer

def show_account(request):
    if request.method == 'POST':
        # Registration process
        if 'register' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            if User.objects.filter(username=username).exists():
                # Handle case when user already exists
                return render(request, 'account.html', {'error': 'Username already taken'})

            # Create user and customer
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  # Automatically hashes the password
            )

            Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            
            # Redirect to the registration success page
            return redirect('registration_success')

        # Login process
        elif 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'account.html', {'error': 'Invalid credentials'})

    return render(request, 'account.html')

def registration_success(request):
    return render(request, 'registration_success.html')

    
