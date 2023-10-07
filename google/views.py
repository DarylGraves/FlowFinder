import googlemaps
import gmaps
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import JsonResponse
from django.conf import settings
import requests
import json
import urllib

# Create your views here.

def home(request):
    context = {}
    return render(request, 'google/home.html',context)

def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'google/map.html',context)

def mydata(request):
    result_list = list(Hydrant.objects\
                .exclude(latitude__isnull=True)\
                .exclude(longitude__isnull=True)\
                .exclude(latitude__exact='')\
                .exclude(longitude__exact='')\
                .values('id',
                        'latitude',
                        'longitude',
                    )
                )
  
    return JsonResponse(result_list, safe=False)