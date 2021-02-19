from django.shortcuts import render
import requests
from django.contrib import messages
from pprint import pprint

# Create your views here.

def weather(request):
                
    url = "http://127.0.0.1:8000/RestApiRestApi/?search={}&"
    headers = {'Authorization': 'Token 0d7a26bad87d36f5782567e99c3d95a3bfa0fe44'}
    city = request.GET.get('city')
    r = requests.get(url.format(city),headers=headers).json()
    pprint(r)
        
    weather={
                'city': city,
                'Description' : r[0]['Description'],
                'Icon': r[0]['Icon'],
                'Temperature':r[0]['Temperature'],
                'Country' : r[0]['Country'],
                'Wind' : r[0]['Wind'],
                }
        
    context = {'weather':weather}
    return render(request,'weather1.html',context)
    