# from .forms import Tranporter_DetailsForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
from django.contrib import messages
from django.contrib import auth
from django.http import *
from django.contrib.auth.models import User
from .models import *
from .forms import TransporterForm
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
#
# def transporter_details(request):
#     if request.method == "POST":
#         form = Tranporter_DetailsForm(request.POST)
#         if form.is_valid():
#             z = form.save()
#             z.save()
#
#     else:
#         form = Tranporter_DetailsForm()
#
#     return render(request, 'customer.html', {'forms': form})

#
# def register1(request):
#     if request.method == 'POST':
#         form = TransporterForm
#         if form.is_valid():
#
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             TransporterForm.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
#                                      password=password)
#
#             user = form.save()
#             messages.success(request, 'user registration successfully')
#             return HttpResponseRedirect('Transporter/register1/')
#
#     else:
#         form = TransporterForm()
#     return render(request, 'registration1.html',{'form': form})
#
#


def register1(request):
    if request.method == 'POST':
        f = TransporterForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login1')

    else:
        f = TransporterForm()

    return render(request, 'registration1.html', {'form': f})


def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return render(request, 'transpoterhome.html')
            else:
                messages.error(request, 'Invalid Username or password')
        else:
            messages.error(request, 'Invalid Username or password')

    form = AuthenticationForm()
    return render(request, 'login1.html', {'form': form})
#
#
def logout(request):
    auth.logout(request)
    messages.info(request,"Logged out Successfully")
    return render(request,'login.html')


def Transporterhome(request):
    return render(request, 'transpoterhome.html')

def Add(request):
    return render(request, 'Addtruck.html')

def View(request):
    return render(request, 'Viewstruck.html')

def update(request):
    return render(request, 'update.html')