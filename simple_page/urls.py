"""Simple API URL Configuration"""

from django.conf.urls import url
from simple_page import views

urlpatterns = [
    url(r'^page/$', views.HomePageView.as_view(), name='home'),
]
