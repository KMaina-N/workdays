import requests
url = "https://public-holiday.p.rapidapi.com/2023/HR"

headers = {
            "X-RapidAPI-Key": "f348a4deabmsh384459329fcaeb9p174eb3jsnac1ac1a8d14d",
            "X-RapidAPI-Host": "public-holiday.p.rapidapi.com"
        }
headers

data = requests.get(url, headers=headers).json()
data

h = []
for i in data:
    m = i['date']
    
    h.append(m)

sat = True
if sat == True:
    weekmask = '1111110'
    print("includes saturday")
else:
    weekmask = '1111100'
    print("does not include saturday")


import calendar

year = 2023
month = 1
weekend = calendar.monthcalendar(year, month)