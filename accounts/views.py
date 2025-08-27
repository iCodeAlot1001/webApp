from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('welcome-home')

def landingPage(request):
    return render(request, 'accounts/welcome-home.html')

@login_required
def home(request):
    return render(request, 'accounts/home.html')