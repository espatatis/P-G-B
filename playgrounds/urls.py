from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from . import views
urlpatterns = [

    path('home/', views.home, name='home'),
    path('<int:venue_id>/', views.detail, name='detail'),
    path('', views.home, name='home'),
]
