from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Register, Login
from django.db import IntegrityError
from django.contrib import auth
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    username = request.user.username  # Get the username of the logged-in user
    return render(request, 'index.html', {'username': username})

def login_register(request):
    return render(request, 'login_register.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('dept_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=name, email=email, password=password)
                register = Register.objects.create(user=user, name=name, email=email, department=department)
                if not Login.objects.filter(email=email).exists():
                    login = Login.objects.create(email=email, password=password)
                return redirect('login_register')  # Redirect to login page after successful registration
            except IntegrityError:
                return render(request, 'login_register.html', {'error': 'Email already exists'})
        else:
            return render(request, 'login_register.html', {'error': 'Passwords do not match'})

from django.contrib.auth.hashers import check_password

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        
        # Retrieve the user object using the email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            # Compare the provided password with the hashed password
            if check_password(password, user.password):
                # Passwords match, log in the user
                auth_login(request, user)
                return redirect('index')  # Redirect to home page after successful login
            else:
                # Passwords don't match
                messages.error(request, 'Invalid username or password. Please try again.')
                return redirect('login_register')
        else:
            # User not found
            messages.error(request, 'User does not exist')
            
    
        return render(request, 'index.html')
    return HttpResponse(status=405)
    
def logout(request):
    auth_logout(request)
    return render(request,'index.html')  # Redirect to the home page after logout

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def form_valid(self, form):
        # Call the parent class's form_valid() method to perform the default behavior
        super().form_valid(form)
        
        # Log in the user after password reset
        user = form.save()
        auth_login(self.request, user)
        
        # Redirect the user to the home page
        return redirect('index')
    
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirect to your desired page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
