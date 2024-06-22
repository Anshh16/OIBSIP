from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

mainwin=Tk()
mainwin.geometry("500x355+300+100")
mainwin.title("Weather")
mainwin.iconbitmap("D:/Weather Application-Python/cloudweather.ico")
mainwin.config(bg="#EFE7BC")
mainwin.resizable(False,False)

def weather():
    try:
        city=locentry.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home=pytz.timezone(result) 
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%I:%M %p")
        clock.config(text=currenttime)
        name.config(text="WEATHER  DETAILS")
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=693e4a99b744aa480bc41da725f5d15c"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        temp= int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        temperature.config(text=(temp,"°C"))
        if temp>35:
            condi.config(text=(condition,"|","FEELS","LIKE","TOO","HOT","!"))
        elif temp>27 and temp<=35:
            condi.config(text=(condition,"|","FEELS","LIKE","MODERATELY","HOT","!"))
        elif temp>20 and temp<=27:
            condi.config(text=(condition,"|","FEELS","LIKE","MODERATE","."))
        elif temp>10 and temp<=20:
            condi.config(text=(condition,"|","FEELS","LIKE","COLD","!"))
        else:
            condi.config(text=(condition,"|","FEELS","LIKE","ICY","COLD","!"))
        wl.config(text=wind)
        hl.config(text=humidity)
        dl.config(text=condition)
        pl.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!") 

font15=('Arial',15,'bold')
font25=('Arial',25,'bold')
font12=('Arial',12,'bold')
font11=('Arial',11,'bold')

searchimg=PhotoImage(file="D:/Weather Application-Python/searchig.png")
searchimglabel=Label(image=searchimg, border=0)
searchimglabel.place(x=23,y=20)

locentry=Entry(mainwin, justify="center", width=33, border=0, font=font15, background='#FA8072')
locentry.place(x=28,y=28)
locentry.focus()

searchicon=PhotoImage(file="D:/Weather Application-Python/searchicon.png")
searchicbutton=Button(image=searchicon, border=0, cursor='hand2', background='#FA8072', activebackground='#FA8072', command=weather)
searchicbutton.place(x=410,y=25)

logoimg=PhotoImage(file="D:/Weather Application-Python/logo2.png")
logolabel=Label(image=logoimg, border=0)
logolabel.place(x=320, y=90)

bottomboximg=PhotoImage(file="D:/Weather Application-Python/bottomimg.png")
bottomlabel=Label(image=bottomboximg, border=0)
bottomlabel.place(x=9, y=265)

temperature=Label(mainwin, font=font25, background="#EFE7BC", foreground="#8B0000")
temperature.place(x=30,y=160)
condi=Label(mainwin, font=font12, background="#EFE7BC")
condi.place(x=30,y=205)

name=Label(mainwin,font=font12, background="#EFE7BC")
name.place(x=30,y=100)
clock=Label(mainwin, font=font15, background="#EFE7BC")
clock.place(x=30,y=130)

labelwind=Label(mainwin, text="WIND", font=font12, background='#FA8072')
labelwind.place(x=35,y=270)

labelhumidity=Label(mainwin, text="HUMIDITY", font=font12, background='#FA8072')
labelhumidity.place(x=113,y=270)

labeldescription=Label(mainwin, text="DESCRIPTION", font=font12, background='#FA8072')
labeldescription.place(x=220,y=270)

labelpressure=Label(mainwin, text="PRESSURE", font=font12, background='#FA8072')
labelpressure.place(x=365,y=270)

wl=Label(mainwin,text="...", font=font11, width=5, background='#FA8072')
wl.place(x=33,y=290)

hl=Label(mainwin,text="...", font=font11, width=8, background='#FA8072')
hl.place(x=115,y=290)

dl=Label(mainwin,text="...", font=font11, width=9, background='#FA8072')
dl.place(x=235,y=290)

pl=Label(mainwin,text="...", font=font11, width=9, background='#FA8072')
pl.place(x=370,y=290)

mainwin.mainloop()
