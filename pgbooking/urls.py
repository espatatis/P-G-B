"""pgbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import namedtuple
from django.contrib import admin
from django.urls import path, include
import playgrounds
import users
from users import views as user_view
from playgrounds import views as pg_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_signup/', user_view.user_reg, name='user-reg'),
    path('vendor_signup/', user_view.ven_reg, name='ven-reg'),
    path('user_login/', user_view.user_login, name='user-login'),
    path('vendor_login/', user_view.ven_login, name='ven-login'),
    path('vendor/', user_view.ven_profile, name='ven-profile'),
    path('user/', user_view.user_profile, name='user-profile'),
    path('listings/', pg_view.listings, name='listings'),
    path('requests/', include('users.urls')),
    path('bookings/', user_view.bookings, name='bookings'),
    path('add_venue/', pg_view.add_venue, name='add'),
    path('logout/', user_view.logout, name='logout'),
    path('', include('playgrounds.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
