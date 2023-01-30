import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

class DCF:
  #Obtained from user (Assumptions):
  growthrate_ebitda = 0.05   #Fixed for now, this will change to variable once we implement base DCF
  growthrate_fcf = 0.10
  rateofreturn = 0.125   #Used for discount array
  discount = []

  

  


  #Obtained from web:
  EBITDA = []
  FCF = []
  years = []



  def __init__(self,ticker,year):
    self.ticker = ticker
    self.year = year
    self.reqFinance = Request(url='https://stockanalysis.com/stocks/{}/financials/'.format(ticker), headers={'User-Agent' : 'Mozilla/5.0'})
    self.reqCashflow = Request(url='https://stockanalysis.com/stocks/{}/financials/cash-flow-statement/'.format(self.ticker), headers={'User-Agent' : 'Mozilla/5.0'})
    
    self.financetable = pd.read_html(urlopen(self.reqFinance).read(), index_col = 0)[0]
    self.cashflowtable = pd.read_html(urlopen(self.reqCashflow).read(), index_col = 0)[0]
    self.years = [str(int(year)),str(int(year)-1),str(int(year)-2),str(int(year)-3), str(int(year)-4)]

    for each in self.years:
      self.setupEBITDA_FCF(each)
    
  
  def setupEBITDA_FCF(self,year):
    self.EBITDA.append(self.financetable[year]['EBITDA'])
    self.FCF.append(self.cashflowtable[year]['Free Cash Flow'])
  
  def setupDiscount(self,rateofreturn):
    rateofreturn /= 100
    for x in range(1,6):
      sol = (1/((1+rateofreturn)**x))
      self.discount.append(sol)

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
print(cfm.EBITDA)  
print(cfm.FCF)
cfm.setupDiscount(12.5)

print(cfm.discount)
#EBITDA (NEED)              
# #->YOY Change, AVG EBITA GROWTH
#Past Free Cash Flow (NEED)
#->YOY Change, AVG Past Free Cashflow
#NOT ON THE WEBSITE
#Assumptions {EBITDA growth rate, free cash flow rate, rate of return, terminal growth rate, ev/evita multiple }



