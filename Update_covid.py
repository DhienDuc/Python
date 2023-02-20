import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('http://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Case : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        t = ToastNotifier()
        t.show_toast("Covid 19 update",text,duration=10)
        time.sleep(120)

update()        

