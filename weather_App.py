import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    API_KEY = "f2baa6e46d647fe10031c3872d01dd81"   # Your API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].title()

            result.set(
                f"🌍 City: {city}\n"
                f"🌡 Temperature: {temp} °C\n"
                f"💧 Humidity: {humidity}%\n"
                f"☁ Weather: {description}"
            )
        elif response.status_code == 404:
            messagebox.showerror("City Not Found", f"'{city}' is not a valid city ❌")
        else:
            messagebox.showerror("Error", "Unable to fetch weather data!")

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Network Error", "Please check your internet connection!")
    except requests.exceptions.Timeout:
        messagebox.showerror("Timeout Error", "Server is taking too long to respond!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")


root = tk.Tk()
root.title("Weather Check")
root.geometry("350x400")
root.resizable(False, False)
root.configure(bg="#1676D6")

tk.Label(
    root,
    text="Weather Check",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1676D6"
).pack(pady=15)

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    bg="#ECF0F1",
    fg="black",
    relief="flat"
)
city_entry.pack(pady=10, ipady=6)


tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#64F2A4",
    fg="black",
    activebackground="#2ECC71",
    relief="flat",
    command=get_weather
).pack(pady=12)


result = tk.StringVar()
tk.Label(
    root,
    textvariable=result,
    font=("Arial", 14),
    fg="white",
    bg="#2C3E50",
    justify="center",
    wraplength=300
).pack(pady=20, ipadx=10, ipady=10)

root.mainloop()