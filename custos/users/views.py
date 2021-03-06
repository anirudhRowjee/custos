from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import json


# importing models
from . import models

def loginview(request):
    """
    login method for the app
    """
    
    if request.method == "POST":
        # log the user in
        data = request.POST
        username = data['username']
        password = data['password']

        # do the actual login
        user = authenticate(username = username, password=password)
        
        if user is not None:
            # login successful
            print(username, password)
            login(request, user)
            return redirect('home')

        else:
            # login failed
            context = {
                'message': "Improper Credentials - Username or Password is Wrong"
            }
            return render(request, 'users/login.html', context)
    else:
        if request.user.is_authenticated:
            # render home page
            return redirect('home')
        return render(request,'users/login.html')

def logoutview(request):
    """
    logs out user
    """
    logout(request)
    return redirect('login')


def registerview(request):
    """
    register a new user 
    """
    if request.method == "POST":
        # log the user in
        data = request.POST
        username = data['username']
        email = data['email']
        password = data['password']
        password_repeat = data['password_repeat']

        # if the repeated password is wrong
        if password != password_repeat:
            context = {'message': "Passwords Don't Match"}
            return render(request, 'signup.html', context)
        else:
            # hash the password
            password_hashed = make_password(password)

            # register user
            user = User(username=username, password=password_hashed, email=email)
            user.save()

            # do the actual login
            user = authenticate(username = username, password=password)
            login(request, user)

            return redirect('home')
    else:
        return render(request,'404.html')


def myaccount(request):
    if request.method == "GET":

        # get the user from request
        uid = request.user.id
        if not uid:
            return JsonResponse(
                {"error": 400, "message": "Please Login to Access this Data"}
            )

        user_profile = models.Profile.objects.get(id=uid)

        if not user_profile:
            return JsonResponse({"error": 400, "message": "user does not exist"})
        
        return render(request, 'users/myaccount.html', {'profile': user_profile})
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data = body['data']

        try:
            # new user details
            username = data.get("username")
            bio = data.get("bio")
            email = data.get('email')
            user_id = int(data.get('user_id'))
        except MultiValueDictKeyError:
            # return JSON request - something wrong
            return JsonResponse({"status": 400, "error": "Incomplete Request Body"})
        
        user = User.objects.get(id=user_id)
        user_profile = models.Profile.objects.get(user=user)

        user.username = username
        user.email = email
        user_profile.bio = bio

        user.save()
        user_profile.save()

        return redirect('myaccount')