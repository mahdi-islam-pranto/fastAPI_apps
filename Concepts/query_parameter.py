import json
from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# load data from json file
def load_data():
    with open('patients.json', 'r') as f:
        return json.load(f)

# get patients data in sorted order (height, weight, bmi, asc/desc) => query parameter
# example:
# set the endpoint like /sort?sort_by=height&order=asc 
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data