from fastapi import FastAPI, Request
import requests
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

class RequestAPI:
    
    url = "https://api.quotable.io/random"
    

    def get_quote(self):
         
        response = requests.get(self.url)

        if response.status_code == 200:
            response = response.json()
        else:
            response = None

        return response
    

    def get_content(self):
        quote = self.get_quote()

        return quote["content"]


    def get_author(self):
        author = self.get_quote()

        return author["author"]
    

    def name_list(self, name):
        names = []
        names.append({name})

        return ", ".join(names)    


    def get_text_with_quote_for_name(self, name):
        names = {
        "Alibek",
        "Zhanna",
        "Timur",
        "Aizhan"
    }
        if name in names:
            result = "Hello, %s! My quote to you is: %s Author: %s" % (name.capitalize(), self.get_content(), self.get_author())
        else:
            result = "there is no such name in the list"
        return result
    

    def get_name_info(self, name):
        info = {
        "Alibek": {
            "sex": "male",
            "age": 25,
            "hobby": "skii",
            "job": "master of sewing holes in a sock",
            "feature":"poorly sees small details"
        },
        "Zhanna": {
            "sex": "female",
            "age": 23,
            "hobby": "paint",
            "job": "Sock Hole Master",
            "feature":"color blind"
        },
        "Timur": {
            "sex": "male",
            "age": 30,
            "hobby": "boxing",
            "job": "professional ballet dancer",
            "feature":"impaired coordination"
        },
        "Aizhan": {
            "sex": "female",
            "age": 51,
            "hobby": "hang out with friends in pub",
            "job": "strip dancer",
            "feature":"limps on the right leg"
        }
    }
        if name in info:
            result =  info[name]
        else:
            result = "there is no such name in the list"   
        return result

    
    def country_list(self):
        country = {
        "USA",
        "China",
        "UK",
        "Australia"
    }
        return ", ".join(country)    
    
    
    def get_country(self, country):
        info = {
            "USA": {
                "President": "Joe Biden",
                "Capital": "Washington, D.C.",
                "National Language": "English",
                "Largest City": "New York City",
                "Motto":"In God We Trust"
            },
            "China": {
                "Government": "Unitary Marxist–Leninist one-party socialist republic",
                "Capital": "Beijing",
                "National Language": "Standard Chinese",
                "Largest City": "Shanghai",
                "Motto":"---"
            },
            "UK": {
                "Government": "Unitary parliamentary constitutional monarchy",
                "Capital": "London",
                "National Language": "English",
                "Largest City": "---",
                "Motto":"---"
            },
            "Australia": {
                "Government": "Federal parliamentary constitutional monarchy",
                "Capital": "Canberra",
                "National Language": "English",
                "Largest City": "Sydney",
                "Motto":"---"
            }
        }
        if country in info:
            result =  info[country]
        else:
            result = "there is no such country in the list"   
        return result
            

my_request = RequestAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request, "greeting": "Hola mi amiga!"})

 
@app.get("/names")
def names(request: Request, name):
    nam = {
        "request": request,
        "n": my_request.name_list(name)
    }

    return templates.TemplateResponse("names.html", nam)
    

@app.get("/quotes")
def db(request: Request):
    parameters = {
        "request": request,
        "content": my_request.get_content(),
        "author": my_request.get_author()
    }
    return templates.TemplateResponse("quotes.html", parameters)

@app.get("/quotes/{name}")
def db(request: Request, name):
    parameters = {
        "request": request,
        "name": name,
        "content": my_request.get_content(),
        "author": my_request.get_author()
    }
    return templates.TemplateResponse("quotes.html", parameters)
    #return my_request.get_text_with_quote_for_name(name)


@app.get("/{name}/info")
def information(request: Request, name):
    infor = {
        "request": request,
        "name": name,
        "in": my_request.get_name_info(name)        
    }
    
    return templates.TemplateResponse("info.html", infor)


@app.get("/country")
def country():

    return my_request.country_list()


@app.get("/country/{country}")
def country_one(country):
    
    return my_request.get_country(country)

@app.get("/about")
def index(request: Request):
    
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("names.html", {"request": request, "id": id})

