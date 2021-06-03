# from .forms import RegistrationForm

from django.http.response import HttpResponse, HttpResponseBadRequest
import playgrounds
from .models import Account
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from playgrounds.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def ven_reg(request):
    ctx = {}

    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        data = request.POST
        if data['password1'] == data['password2']:
            saveuser = Account.objects.create(
                email=data['email'], name=data['name'], phone=data['phone'], password=data['password1'])
            saveuser.save()
            u = Account.objects.get(email=data['email'])
            Venue.objects.create(user=u, venue_name=data['venue_name'], picture=request.FILES['picture'], city=data['city'],
                                 pin=data['pin'], contact=data['contact'], price=data['price'], address=data['address'])

            auth_login(request, saveuser)
            return redirect('user-profile')
        else:
            return HttpResponse(''' <h5 style="font-weight: 700">Wrong credentials</h5> <a href="/vendor_signup">Click here</a> to go to register page ''')

    else:
        form = VendorRegistrationForm()
    return render(request, 'users/ven-reg.html', {'form': form})


def user_reg(request):
    ctx = {}

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = request.POST
            if data['password1'] == data['password2']:
                saveuser = Account.objects.create_user(
                    email=data['email'], name=data['name'], phone=data['phone'], password=data['password1'], is_vendor=False)
                saveuser.save()
                auth_login(request, saveuser)
                return redirect('user-profile')
            else:
                return HttpResponse(''' <h5 style="font-weight: 700">Wrong credentials</h5> <a href="/user_signup">Click here</a> to go to register page ''')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/user-reg.html', {'form': form})


def user_login(request):
    ctx = {}
    if request.method == 'POST':
        print(request.POST['password'])
        form = LoginForm(request.POST)
        data = request.POST
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('user-profile')
        # else:
            # return HttpResponse(''' <h5 style="font-weight: 700">Wrong credentials</h5> <a href="/user_login">Click here</a> to go to login page ''')
    else:
        form = LoginForm()
    return render(request, 'users/user-login.html', {'form': form})


def ven_login(request):
    ctx = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        data = request.POST
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('ven-profile')
        else:
            return HttpResponse(''' <h5 style="font-weight: 700">Wrong credentials</h5> <a href="/vendor_login">Click here</a> to go to login page ''')

    else:
        form = LoginForm()
    return render(request, 'users/ven-login.html', {'form': form})


@login_required(login_url='user-login')
def user_profile(request):
    time = datetime.now() - timedelta(hours=1)
    ctx = {
        'requests_1': Request.objects.filter(user=request.user, request_time__gt=time),
        'requests_2': Request.objects.filter(user=request.user, request_time__lt=time),
    }
    return render(request, 'users/user-profile.html', ctx)


@login_required(login_url='ven-login')
def ven_profile(request):
    user = Account.objects.get(email=request.user.email)
    venue = Venue.objects.filter(user=user)
    ctx = {
        'requests': Request.objects.filter(venue__in=venue),
        'venues': venue,
    }

    return render(request, 'users/ven-profile.html', ctx)


@login_required(login_url='ven-login')
def requests(request):
    user = Account.objects.get(email=request.user.email)
    venue = Venue.objects.filter(user=user)
    ctx = {
        'requests': Request.objects.filter(venue__in=venue),
    }
    return render(request, 'users/requests.html', ctx)


@login_required(login_url='ven-login')
def request_accepted(request, request_id):
    req = Request.objects.get(id=request_id)
    user = req.user
    book = Booking.objects.create(
        user=user, playground=req.venue, from_date=req.from_date, to_date=req.to_date, total=200)
    book.save()
    req.venue.status = True
    req.delete()

    return HttpResponse('''<h5 style="font-weight: 700">Request accepted</h5> <a href="/">Click here</a> to go to home''')


@login_required(login_url='ven-login')
def request_rejected(request, request_id):
    req = Request.objects.get(id=request_id)
    req.delete()
    return HttpResponse('''<h5 style="font-weight: 700">Request deleted/rejected</h5> <a href="{% url 'home' %}">Click here</a> to go to home''')


def bookings(request):
    venue = Venue.objects.filter(user=request.user)
    u_booking = Booking.objects.filter(user=request.user)
    v_booking = Booking.objects.filter(playground__in=venue)
    ctx = {
        'u_bookings': u_booking,
        'v_bookings': v_booking,
    }
    print(request.user)
    return render(request, 'users/bookings.html', ctx)


@login_required(login_url='user-login')
def logout(request):
    user = Account.objects.get(email=request.user.email)
    auth_logout(request)
    return redirect('user-login')
