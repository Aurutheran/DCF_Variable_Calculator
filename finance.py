import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

class DCF:
  #Obtained from user (Assumptions):
  growthrate_ebitda = 0.05   #Fixed for now, this will change to variable once we implement base DCF
  growthrate_fcf = 0.10
   #Used for discount array
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

    try:
      for each in self.years:
        self.setupEBITDA_FCF(each)
    except:
      self.EBITDA = []
      self.FCF = []
      self.setupEBITDA_FCF(self.year)
    finally:
      if len(self.EBITDA) == 1:
        print("Could only print current year cause values are missing")
        print("EBITDA: {}".format(self.EBITDA))
        print("FCF: {}".format(self.FCF))
      else:
        print("EBITDA: {}".format(self.EBITDA))
        print("FCF: {}".format(self.FCF))
        
  def setupEBITDA_FCF(self,year):
    self.EBITDA.append(self.financetable[year]['EBITDA'])
    self.FCF.append(self.cashflowtable[year]['Free Cash Flow'])
    
  
  def setupDiscount(self,rateofreturn):
    rateofreturn /= 100
    for x in range(1,6):
      sol = (1/((1+rateofreturn)**x))
      self.discount.append(sol)

#Main CLASS
print("Enter Ticker-Name: ")
ticker = input()

print("Enter Year: ")
year = input()

cfm = DCF(ticker,year)
cfm.setupDiscount(15.5)

print(cfm.discount)




