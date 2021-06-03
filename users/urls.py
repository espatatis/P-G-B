from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('accepted_<int:request_id>', views.request_accepted, name='req-acc'),
    path('rejected_<int:request_id>', views.request_rejected, name='req-rej'),
    path('', views.requests, name='requests')
]
