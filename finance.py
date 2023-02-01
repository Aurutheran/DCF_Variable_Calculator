import pandas as pd
from urllib.request import Request, urlopen

class DCF:
  #Obtained from user (Assumptions):
  growthrate_ebitda = [] 
  growthrate_fcf = []
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

      print("Here are the web-scrapped values")
      print("EBITDA:".format(self.EBITDA))
      print("FCF:".format(self.FCF))
      self.EBITDA = [int(i)*1000000 for i in self.EBITDA]
      self.FCF = [int(i)*1000000 for i in self.FCF]
        
  def setupEBITDA_FCF(self,year):
    self.EBITDA.append(self.financetable[year]['EBITDA'])
    self.FCF.append(self.cashflowtable[year]['Free Cash Flow'])

    
  
  def setupDiscount(self,rateofreturn):
    value = float(rateofreturn) / 100
    for x in range(1,6):
      sol = (1/((1+value)**x))
      self.discount.append(sol)
    print("The discounts are {}".format(self.discount))



  def setupEBITDA_GR(self, userstring):
    arr = str(userstring).split()

    if len(arr) == 1:
      try:
        self.growthrate_ebitda = [(round(float(arr[0])/100,5)+1) for i in range(0,5)]
        print(self.growthrate_ebitda)
      except:
        print("You have entered an invalid value.")
        print("Enter EBITDA Growth Rate:")
        EBITDA_GR = input() 
        self.setupEBITDA_GR(EBITDA_GR)

    elif len(arr) == 5:
      for each in arr:
        try:
          self.growthrate_ebitda.append(round(float(each)/100,5)+1)
        except:
          print("You have entered an invalid value.")
          print("Enter EBITDA Growth Rate:")
          EBITDA_GR = input() 
          self.setupEBITDA_GR(EBITDA_GR)
    
          
    else:
      print("You have entered an invalid range.")
      print("Enter EBITDA Growth Rate:")
      EBITDA_GR = input() 
      self.setupEBITDA_GR(EBITDA_GR)

#Main CLASS

#Ticker Information
print("Enter Ticker-Name: ")
# ticker = input()
ticker = "AAPL" #REMOVe

#Year Information
print("Enter Year: ")
# year = input()
year = "2022" #REMOVe

#Defining the Object
cfm = DCF(ticker,year)

#Rate of Return Information
print("Enter Rate of Return (EX: 12.5 for 12.5%):")
# ROR = input()
ROR = "12.5"
cfm.setupDiscount(ROR)

#EBITDA Growth Information
print("Enter EBITDA Growth Rate:")
EBITDA_GR = input()
cfm.setupEBITDA_GR(EBITDA_GR)


print("Values in the millions:")
print(cfm.EBITDA)
print(cfm.FCF)


#Free Cashflow Information
print("Enter Free-Cashflow Growth Rate:")
FCF_GR = input()








