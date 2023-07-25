import tkinter as tk
from tkinter import messagebox
import random
import requests

def generate_random_joke():
    joke_api_url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(joke_api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        elif data["type"] == "twopart":
            return f"{data['setup']} {data['delivery']}"
    else:
        return "Failed to fetch joke from the API"

def generate_random_fact():
    fact_api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(fact_api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data["text"]
    else:
        return "Failed to fetch fact from the API"

def show_options():
    # Destroy the "Choose an Option" button
    options_button.destroy()

    # Create "Joke" and "Facts" buttons
    joke_button = tk.Button(root, text="Joke", command=show_joke, font=("Arial", 12))
    joke_button.pack(pady=10)

    fact_button = tk.Button(root, text="Facts", command=show_fact, font=("Arial", 12))
    fact_button.pack(pady=5)

def show_joke():
    joke = generate_random_joke()
    messagebox.showinfo("Random Joke", joke)

def show_fact():
    fact = generate_random_fact()
    messagebox.showinfo("Random Fact", fact)

# Create the main window
root = tk.Tk()
root.title("Fun Joke & Fact Generator")
root.geometry("400x200")

# Add a fun title label
title_label = tk.Label(root, text="Welcome to the Fun Joke & Fact Generator!", font=("Arial", 14))
title_label.pack(pady=10)

# Add a button to show options
options_button = tk.Button(root, text="Choose an Option", command=show_options, font=("Arial", 12))
options_button.pack(pady=20)

# Add a footer label
footer_label = tk.Label(root, text="Have a laugh or learn something new!", font=("Arial", 10))
footer_label.pack(pady=5)

root.mainloop()
