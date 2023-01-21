from django.shortcuts import render
import pandas as pd
import requests
import calendar
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')
def days(request):
    context = {}
    if request.method == 'POST':
        sdate = request.POST.get('start')[0:2]
        edate = request.POST.get('end')[0:2]
        Month = request.POST.get('start')[3:5]
        year = request.POST.get('start')[6:10]
        sat = request.POST.get('sat')
        print('sat', sat)
        print('year', year)
        
        url = f"https://public-holiday.p.rapidapi.com/{year}/HR"

        headers = {
                    "X-RapidAPI-Key": "f348a4deabmsh384459329fcaeb9p174eb3jsnac1ac1a8d14d",
                    "X-RapidAPI-Host": "public-holiday.p.rapidapi.com"
                }
        headers

        data = requests.get(url, headers=headers).json()
        print(data)

        h = []
        for i in data:
            m = i['date']
            
            h.append(m)

        holiday_list = []
        for i in data:
            name = i['localName']
            date = i['date']
            l = [name, date]
            holiday_list.append(l)
        if sat == 'yes':
            weekmask = '1111110'
        else:
            weekmask = '1111100'
        
        offtime = h
        mon = Month
        day1 = sdate
        day2 = edate
        monthly_holidays = []
        name_holidays = []

        for i in offtime:
            if mon in i[5:7]:
                monthly_holidays.append(i[5:7])
        for i in holiday_list:
            if mon in i[1][5:7]:
                print('holiday', i)
                name_holidays.append(i)
        # print('name of holidays:',name_holidays)
        hl = []
        for x in name_holidays:
            h_list = str(x).replace('[', '').replace(']', '').replace("'", '').replace('"', '')
            print('holidays:',name_holidays)
            hl.append(h_list)
        # print('name of holidays:',name_holidays)
        # print(monthly_holidays)
        holidays = len(monthly_holidays)
        month = f'{mon}'
        days = pd.bdate_range(start=f'{year}-{month}-{day1}', end=f'{year}-{month}-{day2}', freq='C', weekmask=weekmask, holidays=offtime).format(formatter=lambda x: x.strftime('%Y-%m-%d %A'))
        print(len(days))
        no_days = len(days)
        y = int(year)
        mn = int(Month)

        satur = calendar.SATURDAY
        sat_matrix = calendar.monthcalendar(y,mn)

        sund = calendar.SUNDAY 
        sund_matrix = calendar.monthcalendar(y,mn)
        
        sat_days = sum(1 for x in sat_matrix if x[satur] != 0)
        sun_days = sum(1 for x in sund_matrix if x[sund] != 0)
        
        if sat_days > sun_days:
            weekends = sat_days
        else:
            weekends = sun_days

        sdate = request.POST.get('start')
        edate = request.POST.get('end')
        context = {'no_days': no_days, 'weekends': weekends, 'holidays':holidays, 'sdate':sdate, 'edate':edate, 'sat':sat, 'name_holidays':hl}
        return render(request, 'home.html', context=context)
   
    return render(request, 'home.html')