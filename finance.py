import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

class DCF:
  EBITDA = []
  FCF = []
  years = []

  def __init__(self,ticker,year):
    self.ticker = ticker
    self.year = year
    self.reqFinance = Request(url='https://stockanalysis.com/stocks/{}/financials/'.format(ticker), headers={'User-Agent' : 'Mozilla/5.0'})
    self.reqCashflow = Request(url='https://stockanalysis.com/stocks/{}/financials/cash-flow-statement/'.format(self.ticker), headers={'User-Agent' : 'Mozilla/5.0'})

    self.EBITDA = []
    self.FCF = []
    self.years = []

    webpage = urlopen(self.reqFinance).read()
    table_MN = pd.read_html(webpage, index_col = 0)
    self.financetable = table_MN[0]

    webpage = urlopen(self.reqCashflow).read()
    table_MN = pd.read_html(webpage, index_col = 0)
    self.cashflowtable = table_MN[0]
  
  #Request 
  # def func_finance(self):
  #   webpage = urlopen(self.reqFinance).read()
  #   table_MN = pd.read_html(webpage, index_col = 0)
  #   return table_MN[0]

  # def func_cashflow(self):
  #   webpage = urlopen(self.reqCashflow).read()
  #   table_MN = pd.read_html(webpage, index_col = 0)
  #   return table_MN[0]


#Main CLASS
print("Enter Ticker-Name: ")
ticker = input()

print("Enter Year: ")
year = input()

cfm = DCF(ticker,year)
cfm.years = [str(int(year)),str(int(year)-1),str(int(year)-2),str(int(year)-3), str(int(year)-4)]

for each in cfm.years:
  cfm.EBITDA.append(cfm.financetable[each]['EBITDA'])
  cfm.FCF.append(cfm.cashflowtable[each]['Free Cash Flow'])
print(cfm.EBITDA)  
print(cfm.FCF)

#EBITDA (NEED)              
# #->YOY Change, AVG EBITA GROWTH
#Past Free Cash Flow (NEED)
#->YOY Change, AVG Past Free Cashflow
#NOT ON THE WEBSITE
#Assumptions {EBITDA growth rate, free cash flow rate, rate of return, terminal growth rate, ev/evita multiple }



