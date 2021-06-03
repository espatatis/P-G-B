from django import forms
from playgrounds.models import *
from .models import *


class VendorRegistrationForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(
        attrs={'class': 'input'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'input'}))
    venue_name = forms.CharField(label='Venue Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    venue_desc = forms.CharField(label='Description', max_length=1000, widget=forms.TextInput(
        attrs={'class': 'input'}))
    size = forms.DecimalField(label='Size (in square feet)', decimal_places=2, max_digits=15,
                              widget=forms.NumberInput(attrs={'class': 'input'}))
    capacity = forms.IntegerField(
        label='Capacity of Stadium (0 if no stadium)', widget=forms.NumberInput(attrs={'class': 'input'}))
    picture = forms.ImageField()
    price = forms.DecimalField(decimal_places=2, max_digits=10,
                               widget=forms.NumberInput(attrs={'class': 'input'}))
    address = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'input'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    pin = forms.CharField(max_length=6, widget=forms.TextInput(
        attrs={'class': 'input'}))
    contact = forms.CharField(label='Venue contact number', max_length=10, widget=forms.TextInput(
        attrs={'class': 'input'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'input'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'input'}))


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input'}), max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input'}))


class ListingForm(forms.Form):
    venue_name = forms.CharField(label='Venue Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    venue_desc = forms.CharField(label='Description', max_length=1000, widget=forms.TextInput(
        attrs={'class': 'input'}))
    size = forms.DecimalField(label='Size (in square feet)', decimal_places=2, max_digits=15,
                              widget=forms.NumberInput(attrs={'class': 'input'}))
    capacity = forms.IntegerField(
        label='Capacity of Stadium (0 if no stadium)', widget=forms.NumberInput(attrs={'class': 'input'}))
    picture = forms.ImageField()
    price = forms.DecimalField(decimal_places=2, max_digits=10,
                               widget=forms.NumberInput(attrs={'class': 'input'}))
    address = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'input'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'input'}))
    pin = forms.CharField(max_length=6, widget=forms.TextInput(
        attrs={'class': 'input'}))
    contact = forms.CharField(label='Venue contact number', max_length=10, widget=forms.TextInput(
        attrs={'class': 'input'}))
