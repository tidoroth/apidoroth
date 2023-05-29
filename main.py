from typing import Union
from fastapi import FastAPI, HTTPException
import pandas as pd
import json
import jwt

df = pd.read_csv('agrogalaxyData.csv')
df = df.fillna('')
dfDict =  df.to_dict(orient='records')


app = FastAPI()

@app.get("/")
def read_root():
    return dfDict


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
