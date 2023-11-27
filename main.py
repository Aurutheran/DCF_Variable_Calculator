#FastAPI Code
import uvicorn
from os import getenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time, os

#Finance Code
import finance
import currentvalue

app = FastAPI()
res = {}
DCFValue = 0
CurrentValue = 0
MarginOfSafety = 0

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

app.mount("/static", StaticFiles(directory="static"), name="static") #html_css

templates = Jinja2Templates(directory="html_css") #html_css

@app.get('/')
def render(request: Request):
    #return templates.TemplateResponse("item.html", {"request": request, "DCFValue": 0, "CurrentValue": 0, "MarginOfSafety": 0})
    return templates.TemplateResponse("item.html", {"request": request, "DCFValue": DCFValue, "CurrentValue": CurrentValue, "MarginOfSafety": MarginOfSafety})

@app.post('/')
async def run(request: Request):
    data = await request.form()
    res.update(data)
    print(data)
    ticker = res['ticker']
    year = res['year']
    ror = res['ROR']
    ev_ebidta = res['EV/EBIDTA']
    Terminal_ROR = res['TerminalROR']
    ebidta_gr = res['EBIDTA_GR']
    fcf = res['FCF']

    cfm = finance.DCF(ticker, year)
    cfm.setupDiscount(ror)
    cfm.setEV_EBITDA(ev_ebidta)
    cfm.setupTerminal(Terminal_ROR)
    cfm.setupEBITDA_GR(ebidta_gr)
    cfm.setupFCF_GR(fcf)

    cfm.obtainGrowthMethod()
    cfm.setGrowthAverage()
    cfm.obtainSharePrice()

    DCFValue = round(cfm.Share_Price,2)

    print('Please wait, your requests are being processed')
    time.sleep(10)
    cfm.cls()

    curval = currentvalue.CurVal(ticker)
    CurrentValue = round(curval.getcurval(), 2)

    MarginOfSafety = round(float(DCFValue-CurrentValue)/float(DCFValue)*100, 2)

    return templates.TemplateResponse("item.html", {"request": request, "data": data, "DCFValue": DCFValue, "CurrentValue": CurrentValue, "MarginOfSafety": MarginOfSafety})

@app.get('/getval')
def val():
    return {"results": res}