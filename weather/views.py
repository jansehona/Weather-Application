# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def homepage(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4b21ce9330eebdc1012c9d771ebe427a'
    return render(request, 'loginPage/homepage.html')

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) 
    
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/weather')
    else:
        form = UserCreationForm()
    
    args = {'form': form}
    return render(request, 'loginPage/registration_form.html', args)


