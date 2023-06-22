from django.shortcuts import render

# Create your views here.
import json
import urllib.request
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        res =  urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=84fb46aecf44745d4c1740a57a6f2397").read()
        python_obj = json.loads(res)
        data  = {
            'city_name': str(python_obj['name']),
            'city_temp': str(python_obj['main']['temp']),
            'city_visibility': str(python_obj['visibility']),
            'city_wind_speed': str(python_obj['wind']['speed'])
        }
        return render(request, 'whether-home.html',data)
    else:
        city = ' '
        return render(request, 'whether-home.html')