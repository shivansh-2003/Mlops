from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
try:
    model = joblib.load("model.pkl")  # Adjusted path
except Exception as e:
    raise RuntimeError("Model loading failed: " + str(e))

# Define the FastAPI app
app = FastAPI()

# Define the request body using Pydantic
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Flower Prediction API"}

# Define a POST endpoint for predictions
@app.post("/predict")
def predict(iris: IrisRequest):
    # Convert input data to the correct format
    input_data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    
    # Make prediction
    try:
        prediction = model.predict(input_data)
        species = {0: "setosa", 1: "versicolor", 2: "virginica"}
        return {"prediction": species[prediction[0]]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction failed: " + str(e))