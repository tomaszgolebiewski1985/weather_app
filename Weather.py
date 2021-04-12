from tkinter import *
import requests
import json
from PIL import ImageTk, Image

root = Tk()
root.title("Aktualna pogoda")
root.geometry("250x300")


def city_lookup():
    try:
    	global weather_image
    	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&units=metric&appid=##############")
    	api = json.loads(api_request.content)
    	# print(json.dumps(api, indent=4, sort_keys=True))
    	wt_feels_like = int(api["main"]["feels_like"])
    	wt_humidity = int(api["main"]["humidity"])
    	wt_pressure = int(api["main"]["pressure"])
    	wt_temperature = int(api["main"]["temp"])
    	wt_temperature_max = int(api["main"]["temp_max"])
    	wt_temperature_min = int(api["main"]["temp_min"])
    	wt_weather = api["weather"][0]["icon"]
    	wt_city = api["name"]
    	# print(wt_weather)
    	# print(wt_city)
    	# print(wt_humidity)
    	# print(wt_feels_like)
    	# print(wt_pressure)
    	# print(wt_temperature)
    	# print(wt_temperature_max)
    	# print(wt_temperature_min)
    	temperature_label.config(text=wt_temperature)
    	city_label.config(text=wt_city)
    	temp_min_label.config(text=f'Temp. min: {wt_temperature_min}')
    	temp_max_label.config(text=f'Temp. max: {wt_temperature_max}')
    	humidity_label.config(text=f'Wilgotność: {wt_humidity}%')
    	pressure_label.config(text=f'Ciśnienie: {wt_pressure} hpa')
    	city_entry.delete(0, END)
    	temperature_label_2.config(text="Stopni Celsjusza")
    	weather_image = ImageTk.PhotoImage(Image.open(f'{wt_weather}.png'))
    	weather_state_label.config(image=weather_image)
    except Exception as e:
    	message = "Connection Error :("
    	temperature_label.config(text=message)


city_entry = Entry(root)
city_entry.grid(row=0,column=0, padx=5, pady=5)    

submit_button = Button(root, text="Sprawdź pogodę", command=city_lookup)
submit_button.grid(row=0, column=1, padx=5, pady=5)

city_label = Label(root, text="", font=('Helvetica', 16))
city_label.grid(row=1, column=0, columnspan=2)

temperature_label = Label(root, text="", font=('Helvetica', 30))
temperature_label.grid(row=2, column=0)

temperature_label_2 = Label(root, text="")
temperature_label_2.grid(row=3, column=0)

temp_min_label = Label(root, text="")
temp_min_label.grid(row=4, column=0)

temp_max_label = Label(root, text="")
temp_max_label.grid(row=4, column=1)

humidity_label = Label(root, text="")
humidity_label.grid(row=5, column=0)

pressure_label = Label(root, text="")
pressure_label.grid(row=5, column=1)

weather_state_label = Label(root)
weather_state_label.grid(row=2, column=1, rowspan=2)

root.mainloop()
