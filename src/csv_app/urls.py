from django.urls import path
from .views import csv_homepage_view, posted_csv_view

app_name = 'csv_app'

urlpatterns = [
    path('', csv_homepage_view, name='home'),
    path('/post', posted_csv_view, name='post')
]