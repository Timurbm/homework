"""
from fastapi import FastAPI
import requests 

app = FastAPI()

@app.get("/")
def index():
    return "Welcome"

@app.get("/names")
def names():
    names = {
        "Alibek",
        "Zhanna",
        "Timur",
        "Aizhan"
    }

    for n in names:
        print(n)
    #return "Alibek, Aizhan, Timur, Zhanna"

@app.get("/names/{name}")
def greetings(name):
    url = "https://api.quotable.io/random"
    response = requests.get(url).json()
    result = "Hello, %s! My quote to you is: %s" % (name.capitalize(), response["content"]) 
    return result
    #"Welcome, %s!" % name.capitalize()
"""