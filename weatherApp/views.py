import urllib.request
import json
from django.shortcuts import render
import os

def index(request):
    if request.method == 'POST': 
        city = request.POST['city']
        api_key = os.getenv('OPENWEATHERMAP_API_KEY')  # Mendapatkan API Key dari .env
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').read()
        
        list_of_data = json.loads(source)

        data = {
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + 'C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : (list_of_data['weather'][0]['icon']),   
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
