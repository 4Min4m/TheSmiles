import requests

def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        elif data["type"] == "twopart":
            return f"{data['setup']} {data['delivery']}"
    else:
        return "Failed to fetch joke from the API"

if __name__ == "__main__":
    joke = fetch_random_joke()
    print(joke)
