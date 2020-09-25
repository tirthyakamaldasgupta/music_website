from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import sessions, messages, auth
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import AdditionalListenerDetail, AdditionalArtistDetail

def register(request):
    if request.method == "POST":
        userregistrationform = UserRegisterForm(request.POST)
        if userregistrationform.is_valid():
            userregistrationform.save()
            username = userregistrationform.cleaned_data['username']
            user = User.objects.get(username = username)
            print(userregistrationform.cleaned_data['type_of_users'])
            if userregistrationform.cleaned_data['type_of_users'] == '1':
                addaddtionallistenerdetails = AdditionalListenerDetail(user = user)
                addaddtionallistenerdetails.save()
            elif userregistrationform.cleaned_data['type_of_users'] == '2':
                addaddtionalartistdetails = AdditionalArtistDetail(user = user)
                addaddtionalartistdetails.save()
            return redirect('login')
    else:
        userregistrationform = UserRegisterForm()
    return render(request, 'user/user_register.html', {'userregistrationform' : userregistrationform})

def login(request):
    if request.method == "POST":
        userloginform = AuthenticationForm(request, request.POST)
        if userloginform.is_valid():
            username = userloginform.cleaned_data.get('username')
            password = userloginform.cleaned_data.get('password')
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Wrong username or password provided!')
        else:
            messages.error(request, 'Wrong username or password provided!')
    userloginform = AuthenticationForm()
    return render(request, 'user/user_login.html', {'userloginform' : userloginform})

def logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'additionallistenerdetail') == True:
            return render(request, 'user/listener_dashboard.html', {'user' : user})
        elif hasattr(user, 'additionalartistdetail') == True:
            return render(request, 'user/artist_dashboard.html', {'user' : user})
    

