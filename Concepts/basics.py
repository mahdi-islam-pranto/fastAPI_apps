from fastapi import FastAPI
import json

app = FastAPI()

# make a request 
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

# create a function to load data from a file
def load_data():
    with open('patients.json', 'r') as f:
        return json.load(f)

# get the all data from the json file
@app.get('/view')
def view():
    data = load_data()

    return data