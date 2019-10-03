from django import forms
from .models import *
from django.contrib.auth.models import User
from .models import BOOK




class Userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter username'}
    ), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email ID'}
    ), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
    ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter last name'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ), required=True, max_length=50)

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}
    ), required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username','email','first_name','last_name','password']

# class loginform(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter username'}
#     ), required=True, max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter password'}
#     ), required=True, max_length=50)
#
#     class Meta():
#         model = User
#         fields = ['username','password']

# class Bookingform(forms.ModelForm):
#     class Meta():
#         model = Booking
#         fields = ['Type_of_transport','Company_name',' Name','Telephone_no',' Email_id','Country','City',' Address']


class BOOKForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter username'}
    # ), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Firstname'}
    ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Lastname'}
    ), required=True, max_length=50)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Email'}
    ), required=True, max_length=50)
    contact = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Contact'}
    ), required=True, max_length=50)
    No_of_Boxes = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'No. of Boxes'}
    ), required=True, max_length=50)
    capacity = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Capacity'}
    ), required=True)

    class Meta:
        model = BOOK
        fields = ['first_name','last_name','email','contact','No_of_Boxes','capacity']
