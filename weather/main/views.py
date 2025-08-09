from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
# Create your views here.

load_dotenv()

api_key = os.getenv("API_KEY")


def index(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name").strip()
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metrics&appid={api_key}"
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            context = {
                "country_code": data["sys"]["country"].strip(),
                "description":data["weather"][0]["description"].strip(),
                "pressure": data["main"]["pressure"],
                "humidity":data["main"]["humidity"],
                "temp":data["main"]["temp"],
            }
            
            return render(request, "index.html", context)
        
        else:
            return render(request, "index.html", {"error":response.status_code})
    
    return render(request, "index.html")