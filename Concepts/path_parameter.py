from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

# load data from json file
def load_data():
    with open('patients.json', 'r') as f:
        return json.load(f)
    
# view all patients
# data = load_data()
# print(data)

# view specific patient with a patient_id in the path
@app.get('/patient/{patient_id}')
# patient_id is a path parameter
def view_patient(
    patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')
    ):
    # load all the patients
    data = load_data()
    # check if the patient_id exists
    if patient_id in data:
        return data[patient_id]
    # if not, raise an exception
    raise HTTPException(status_code=404, detail='Patient not found')