from fastapi import FastAPI, Form
from pydantic import BaseModel


class Inputs(BaseModel):
    ticker: str
    year: int
    # rateofreturn: float
    # ebitdamultiple: int
    # EBITDA_GROWTH: float
    # CASH_GROWTH: float
    # TERMINAL_GROWTH: float

# class DCF:
#     ticker = None
#     year = None
#     def __init__(self,ticker,year):
#         self.ticker = ticker
#         self.year = year

global ticker_1
global year_1

app = FastAPI()

# @app.post("/")
# async def root(userinput: Inputs):
#     return {"message":userinput}

# @app.get("/")
# async def getValues():
#     return Inputs.ticker

# @app.get('/')
# def index():
#     return{"Root Directory" : "This is the root directory"}

# @app.get('/DCF/')
# def show(id:int, age:int):
#     return{"Here is the id":id,"Here is the age":age}

@app.post('/ticker/')
def postTicker(input: Inputs):
    return {"message" : input['ticker']}
    

# @app.get('/')
# async def getValues():
#     return {'Ticker': ticker_1, "Year": year_1}

