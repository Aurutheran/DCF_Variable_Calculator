import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

#----------------------------------------------
#Data-Structures
#Constants
million = 1000000

#EBITDA Web-Scraped Values
EBITDA = {}
EBITDA_YOY = {}

#FCF Web-Scraped Values
FCF = {}
#----------------------------------------------



#tickername = input().lower()    #USED TO OBTAIN TICKER TAG NAME
tickername = 'aapl'   #Comment this when we do live implementation and uncomment above

#print("Provide the year to start the DCF:")   
#year = input() #Allows for DCF model to render for whichever year
year = "2022"
years = [year,str(int(year)-1),str(int(year)-2),str(int(year)-3),str(int(year)-4)]


#Financial Information
financialreq = Request(url='https://stockanalysis.com/stocks/{}/financials/'.format(tickername), headers={'User-Agent' : 'Mozilla/5.0'})
financials = urlopen(financialreq).read()
table_finance = pd.read_html(financials)
t_finance = table_finance[0]
print(t_finance)
t_finance.columns = years

cashflowreq = Request(url='https://stockanalysis.com/stocks/{}/financials/cash-flow-statement/'.format(tickername), headers={'User-Agent' : 'Mozilla/5.0'})
cashflows = urlopen(cashflowreq).read()
table_cashflow = pd.read_html(cashflows)
#print(table_cashflow[0]['2022'][0:])



# for each in years:
#   EBITDA[each] = table_finance[0][each][28]
#   FCF[each] = table_cashflow[0][each][17]



# print(EBITDA)
# print(FCF)




  #EBITDA (NEED)
    #->YOY Change, AVG EBITA GROWTH
  #Past Free Cash Flow (NEED)
    #->YOY Change, AVG Past Free Cashflow
  #NOT ON THE WEBSITE
    #Assumptions {EBITDA growth rate, free cash flow rate, rate of return, terminal growth rate, ev/evita multiple }
