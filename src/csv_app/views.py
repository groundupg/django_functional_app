from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import CSVForm
from . import utilities

@require_http_methods(['GET'])
def csv_homepage_view(request:HttpRequest) -> HttpResponse:
    form = CSVForm() 
    return render(request, 'csv/csv_home.html', {'form': form})

#@require_http_methods(['POST'])
#def posted_csv_view(request:HttpRequest) -> HttpResponse:
    