from django.conf.urls import url
from . import views
from django.contrib.auth.views import login as auth_views

urlpatterns = [
    url(r'^$', auth_views, name= 'login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^accounts/login/$', auth_views, name='login'),  # If user is not login it will redirect to login page
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='success'),
    url(r'^home/$', views.home, name='home'),
]
