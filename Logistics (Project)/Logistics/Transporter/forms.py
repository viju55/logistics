from django import forms
#from .models import Tranporter_Details
from .models import *


# class Tranporter_DetailsForm(forms.Form):
#     class Meta:
#         model = Tranporter_Details
#         fields = ['Name','Age','Photograph','Vehicle_Number','License_Number']

class TransporterForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'class':'form-control','placeholder':'Enter username'}
    # ), required=True, max_length=50)
    # email = forms.CharField(widget=forms.EmailInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter email ID'}
    # ), required=True, max_length=50)
    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
    # ), required=True, max_length=50)
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter last name'}
    # ), required=True, max_length=50)
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    # ), required=True, max_length=50)
    #
    # confirm_password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Confirm password'}
    # ), required=True, max_length=50)

    class Meta:
        model = Transporter
        fields = ['username','email','first_name','last_name','password']
