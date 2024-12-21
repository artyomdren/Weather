from tkinter import *
import requests

root = Tk()


# URL = https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather():
    city = cityField.get()

    key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {round(weather["main"]["temp"])}'


root['bg'] = '#fafafa'
root.title("Weather app")
root.geometry('400x350')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='lightblue', bd=50)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

button = Button(frame_top, text='Check the weather', bg='yellow', command=get_weather)
button.pack()

info = Label(frame_bottom, text='Weather info', bg='#ffb700', font=40)
info.pack()

root.mainloop()
