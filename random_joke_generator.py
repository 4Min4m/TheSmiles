import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

def generate_random_joke():
    return random.choice(jokes)

if __name__ == "__main__":
    joke = generate_random_joke()
    print(joke)
