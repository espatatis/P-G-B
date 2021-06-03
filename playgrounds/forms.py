from django import forms
from users.models import *
from .models import *
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.Form):
    From = forms.DateField(widget=DateInput(
        attrs={'min': datetime.date.today() + datetime.timedelta(days=1), 'style': 'width:100%;'}))
    To = forms.DateField(widget=DateInput(
        attrs={'min': datetime.date.today() + datetime.timedelta(days=1), 'style': 'width:100%;'}))
