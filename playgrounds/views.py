from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from users.forms import *
import datetime
from django.contrib import messages
# Create your views here.


def home(request):
    ctx = {}
    return render(request, 'playgrounds/home.html', ctx)


def listings(request):
    ctx = {
        'listings': Venue.objects.all(),
    }
    return render(request, 'playgrounds/listings.html', ctx)


def detail(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = BookingForm()
    ctx = {
        'venue': venue,
        'date': datetime.datetime.now(),
        'form': form,
    }
    if request.method == 'POST':
        if request.user.is_vendor:
            return HttpResponse('''<h5 style="font-weight: 700">Vendor's cannot book grounds</h5> <a href="{% url 'home' %}">Click here</a> to go to home''')
        elif request.user.is_authenticated == False:
            return HttpResponse(request, '<h5> You are not logged in </h5>')
        else:
            form = BookingForm(request.POST)
            data = request.POST
            from_date = data['From']
            to_date = data['To']
            user = Account.objects.get(email=request.user.email)
            Request.objects.create(from_date=from_date,
                                   to_date=to_date, venue=venue, user=user)
            if request.user.is_vendor:
                return redirect('ven-profile')
            else:
                return redirect('user-profile')

    return render(request, 'playgrounds/detail.html', ctx)


def add_venue(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        u = request.user
        data = request.POST
        print(request.FILES)
        Venue.objects.create(user=u, venue_name=data['venue_name'], picture=request.FILES['picture'], city=data['city'],
                             pin=data['pin'], contact=data['contact'], price=data['price'], address=data['address'])
        return redirect('listings')
    else:
        form = ListingForm()
        return render(request, 'playgrounds/add_venue.html', {'form': form})
