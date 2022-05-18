from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, ProfileForm
from .models import UserProfile, Account
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# User Register View

def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('UserProfile')
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            user.save()

            # Create User Profile
            profile = UserProfile()
            profile.user_id = user.id
            profile.save()
            return redirect('login')

    context = {
        'form' : form
    }
    return render(request, 'auth/register.html', context)

# User Login View

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('UserProfile')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('UserProfile')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    return render(request, 'auth/login.html')

# User Logout View

@login_required(login_url='login')
def LogoutUser(request):
    logout(request)
    return redirect('login')

# User Profile 

@login_required(login_url='login')
def Profile(request):
    user = get_object_or_404(UserProfile, user=request.user)
    coder = request.user
    context = {
        'user' : user,
        'coder' : coder
    }
    return render(request, 'auth/profile.html', context)

# Profile Edit view

@login_required(login_url='login')
def EditProfile(request):
    coder = request.user
    user = get_object_or_404(UserProfile, user=request.user)
    form = ProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.save()
        return redirect('UserProfile')
    else:
        print('cant save')
    context = {
        'form' : form,
        'user': user,
        'coder' : coder
    }

    return render(request, 'auth/profile/editprofile.html', context)


# Drivers Profile View

def DriverProfile(request, pk):
    user = get_object_or_404(UserProfile, user=request.user)
    driver = get_object_or_404(UserProfile, pk=pk)
    coder = request.user
    context = {
        'driver' : driver,
        'user' : user,
        'coder': coder
    }
    return render(request, 'profiles/driver_profile.html', context)

