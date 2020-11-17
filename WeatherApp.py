import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}

def format_response(weather_json):
    try:
        name = weather_json['name'] + ", " + weather_json['sys']['country']
        desc = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']

        ret = "City: %s \nConditions: %s \nTemperature: %s °F" % (name, desc, temp)

    except:
        ret = "There was a problem \nretrieving that \ninformation :(" \

    return ret

def get_weather(city):
    weather_key = "[API KEY HERE]"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'APPID': weather_key,
        'q': city,
        'units': 'imperial'
    }
    response = requests.get(url, params=params)
    weather = response.json()
    # print(weather)

    label['text'] = format_response(weather)


root = tk.Tk()
root.minsize(WIDTH, HEIGHT)
root.title("Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./img.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg='white', font=('Times New Roman', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Times New Roman', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="", font=('Courier', 17))
label.place(relwidth=1, relheight=1)





root.mainloop()
