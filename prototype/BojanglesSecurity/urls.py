# MajorHelp/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from MajorHelp.views import * # about,contact, SearchView, SchoolResultsView, DepartmentResultsView, LeaveReview

app_name = "MajorHelp"

urlpatterns = [
    path()
]