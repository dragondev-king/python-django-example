"""Simple API URL Configuration"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from simple_api import views

urlpatterns = [
    url(r'^todo/$', views.TodoList.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
