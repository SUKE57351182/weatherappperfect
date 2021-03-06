from django.shortcuts import render
import requests





# Create your views here.
def index(request):
    return render(request,"./weatherapp2/weather.html")
    

def cityform(request):
    #units=metricで摂氏温度を求める
    url="http://api.openweathermap.org/data/2.5/weather?q={},jp&units=metric&lang=ja&appid=ce675e378018e0201a22230fd2455e12"
    #POSTでデータを受け取る
    if request.POST['city']:
        city = request.POST['city']
        
        
    r = requests.get(url.format(city)).json()


    city_weather ={
        #都市名
        "city":city,
        #天気情報
        "description":r["weather"][0]["description"],
        #最高気温
        "temperature":r["main"]["temp_max"],
        #最低気温
        "temperature2":r["main"]["temp_min"],
        #湿度
        "humidity":r["main"]["humidity"],
        #天気画像
        "icon":r['weather'][0]['icon'],
    }

    

    context={"city_weather" :city_weather}

    return render(request,"./weatherapp2/result.html",context)
    
    