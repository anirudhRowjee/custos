from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout


def Login(request):
    """"""
    if request.user.is_authenticated:
        pass
    else:
        if request.method == 'POST':
            data = request.POST
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
            else:
                return redirect('login')

def Logout(request):
    logout(request)
    return redirect('login')


def Signup(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        email = data['email']
        password = data['password']
        password_repeat = data['password_repeat']
        if password != password_repeat:
            return render(request, 'signup.html', {'error': "Passwords Dont Match"})
        else:
            password_hashed = make_password(password)
            user = u_models.User(username=username, password=password_hashed)
            user.save()
            user_profile = u_models.UserProfile(
                user=user, birth_date=dob, contact=contact)
            user_profile.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')