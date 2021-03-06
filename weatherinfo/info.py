import requests
# Create your views here
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ce675e378018e0201a22230fd2455e12"
    city = "TOKYO"

    r = requests.get(url.format(city)).json()
    print(r.text)