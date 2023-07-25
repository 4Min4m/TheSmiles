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

def show_joke():
    joke = generate_random_joke()
    messagebox.showinfo("Random Joke", joke)

def show_fact():
    fact = generate_random_fact()
    messagebox.showinfo("Random Fact", fact)

root = tk.Tk()
root.title("Fun Joke & Fact Generator")
root.geometry("400x200")

options_button = tk.Button(root, text="Joke =D", command=show_joke)
options_button.pack(side=tk.LEFT, padx=10, pady=10)

options_button = tk.Button(root, text="Facts ;)", command=show_fact)
options_button.pack(side=tk.RIGHT, padx=10, pady=10)


root.mainloop()