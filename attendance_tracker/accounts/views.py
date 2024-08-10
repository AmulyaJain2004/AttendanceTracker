from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignInForm
from .forms import SignUpForm
from .models import CustomUser
from .forms import ForgotPasswordForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, 'Sign-up successful!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Sign-in successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                messages.success(request, 'Password reset successful. You are now logged in.')
                return redirect('home')
            else:
                messages.error(request, 'User does not exist.')
                return redirect('forgotpwd')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgotpwd.html', {'form': form})


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'user': request.user})