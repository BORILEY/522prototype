from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from BojanglesSecurity.views import * # about,contact, SearchView, SchoolResultsView, DepartmentResultsView, LeaveReview

app_name = "BojanglesSecurity"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("device/<int:pk>/", views.DeviceSettingsView.as_view(), name="device"),
    path('update-privacy-setting/', views.update_privacy_setting, name='update_privacy_setting'),
]