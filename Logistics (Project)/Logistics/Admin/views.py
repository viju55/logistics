from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
from django.contrib import messages
from django.contrib import auth
from django.http import *
from django.contrib.auth.models import User

#from Logistics.Admin.forms import BOOKForm
from .models import *
from .forms import BOOKForm,Userform
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def base(request):
    return render(request, 'base.html')


# def product_detail(request):
#     return render(request,'list.html')

# def About(request):
#     return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')


def home(request):
    return render(request, 'home.html')


def air(request):
    return render(request, 'air.html')


def ocean(request):
    return render(request, 'ocean.html')


def ground(request):
    return render(request, 'ground.html')


def register(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                     password=password)
            messages.success(request, 'user registration successfully')
            return HttpResponseRedirect('/register/')
    else:
        form = Userform()
    return render(request, "registration.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return render(request, 'userhome.html')
            else:
                messages.error(request, 'Invalid Username or password')
        else:
            messages.error(request, 'Invalid Username or password')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.info(request,"Logged out Successfully")
    return render(request,'login.html')

def userhome(request):
    return render(request, 'userhome.html')


def air1(request):
    return render(request, 'airfright.html')


def ocean1(request):
    return render(request, 'oceanfright.html')


def groundfright(request):
    return render(request, 'groundfright.html')

# def login(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#     if form.is_valid():
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         User = authenticate(username=username, password=password)
#         return redirect('base.html')
#     else:
#         form = AuthenticationForm()
#     return render(request,'login.html',{'form':form})


# def booking(request):
#     return render(request, 'booking.html')

# def Booking(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#
#
#             return HttpResponseRedirect('/Booking/')
#     else:
#         form = BookingForm()
#
#     return render(request, 'booking.html', {'form': form})

def BOOK(request):
    if request.method == "POST":
        form = BOOKForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/BOOK')
    else:
        form = BOOKForm()
    return render(request,'BOOK.html',{'form':form})

#
# def BOOK(request):
#     if request.method == 'POST':
#
#         form = BOOKForm(request.POST)
#         if form.is_valid():
#             # first_name = request.POST.get('first_name')
#             # last_name = request.POST.get('last_name')
#             # email = request.POST.get('email')
#             # contact = request.POST.get('contact')
#             # No_of_Boxes = request.POST.get('No_of_Boxes')
#             # capacity = request.POST.get('capacity')
#             # #Date = request.POST.get('Date')
#             #
#             # c = BOOK(first_name=first_name,last_name=last_name,email=email,contact=contact,No_of_Boxes=No_of_Boxes,capacity=capacity)
#             # c.save()
#             return HttpResponseRedirect('BOOK/')
#     else:
#         BOOKForm = BOOKForm()
#     return render(request, "BOOK.html",{'form':BOOKForm})


# def BOOK(request):
#     if request.method == "POST":
#         form = BOOKForm(request.POST)
#         if form.is_valid():
#             try:
#                 return redirect("/BOOK/")
#             except:
#                 pass
#     else:
#         form = BOOKForm()
#     return render(request,'BOOK.html',{'form':form})
