import tkinter as tk
import requests

WIDTH = 700
HEIGHT = 600

#api.openweathermap.org/data/2.5/weather?q=London

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
    
        final_str = 'City : %s \nConditions : %s \nTemp : %s' %(name, desc, temp)
    
    except:
        final_str = 'Invalid Name'

    return final_str

def get_weather(city):
    key_no = 'apikeynogoeshere'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : key_no, 'q' : city, 'units' : 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()
root.title("My Weather App")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

frame = tk.Frame(root, bg = 'black')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

lower_frame = tk.Frame(root, bg = 'black', bd = 4)
lower_frame.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.6)

entry = tk.Entry(frame, bg = 'white', font = ('Futura-Light', 18))
entry.place(relx = 0.02, rely = 0.1, relwidth = 0.65, relheight = 0.8)
entry.bind('<Return>', (lambda event: get_weather(entry.get())))

button = tk.Button(frame, bg = 'white', text = 'Get Weather', font = ('Futura-Light', 18), command = lambda : get_weather(entry.get()))
button.place(relx = 0.7, rely = 0.1, relwidth = 0.28, relheight = 0.8)

label = tk.Label(lower_frame, bg = 'white', bd = 4, font = ('Futura-Light', 18), anchor = 'nw', justify = 'left')
label.place(relheight = 1, relwidth = 1)



root.mainloop()
