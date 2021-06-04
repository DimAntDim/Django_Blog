from django.contrib import admin
from django.urls import path
from .views import landing_page, quotes

urlpatterns = [
    path('', landing_page),
    path('quotes/', quotes)
]