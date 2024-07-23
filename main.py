from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI()

# Cargar datos de ejemplo
data = pd.read_csv('data/sample_data.csv')

class DataRequest(BaseModel):
    column: str

@app.get("/")
def read_root():
    """
    Endpoint de prueba para verificar que la API está funcionando.
    """
    return {"message": "Welcome to the Data Analytics API"}

@app.post("/mean")
def calculate_mean(request: DataRequest):
    """
    Calcula la media de una columna específica en los datos.
    :param request: Solicitud que contiene el nombre de la columna.
    :return: Media de la columna.
    """
    if request.column not in data.columns:
        raise HTTPException(status_code=404, detail="Column not found")
    mean_value = data[request.column].mean()
    return {"mean": mean_value}

@app.post("/sum")
def calculate_sum(request: DataRequest):
    """
    Calcula la suma de una columna específica en los datos.
    :param request: Solicitud que contiene el nombre de la columna.
    :return: Suma de la columna.
    """
    if request.column not in data.columns:
        raise HTTPException(status_code=404, detail="Column not found")
    sum_value = data[request.column].sum()
    return {"sum": sum_value}

@app.post("/describe")
def describe_column(request: DataRequest):
    """
    Proporciona una descripción estadística de una columna específica en los datos.
    :param request: Solicitud que contiene el nombre de la columna.
    :return: Descripción estadística de la columna.
    """
    if request.column not in data.columns:
        raise HTTPException(status_code=404, detail="Column not found")
    description = data[request.column].describe().to_dict()
    return {"description": description}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
