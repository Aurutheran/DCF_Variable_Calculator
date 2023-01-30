import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

EBITDA = []
FCF = []
years = []
# tickername = input()
tickername = 'AAPL'

year = '2021'
years = [str(int(year)),str(int(year)-1),str(int(year)-2),str(int(year)-3), str(int(year)-4)]
print(years)

req = Request(url='https://stockanalysis.com/stocks/{}/financials/'.format(tickername), headers={'User-Agent' : 'Mozilla/5.0'})
webpage = urlopen(req).read()
table_MN = pd.read_html(webpage, index_col = 0)
df = table_MN[0]

req2 = Request(url='https://stockanalysis.com/stocks/{}/financials/cash-flow-statement/'.format(tickername), headers={'User-Agent' : 'Mozilla/5.0'})
webpage1 = urlopen(req2).read()
table_MN2 = pd.read_html(webpage1, index_col=0)
df2 = table_MN2[0]

for each in years:
  EBITDA.append(df[each]['EBITDA'])
  FCF.append(df2[each]['Free Cash Flow'])
print(EBITDA)  
print(FCF)

#EBITDA (NEED)              
# #->YOY Change, AVG EBITA GROWTH
#Past Free Cash Flow (NEED)
#->YOY Change, AVG Past Free Cashflow
#NOT ON THE WEBSITE
#Assumptions {EBITDA growth rate, free cash flow rate, rate of return, terminal growth rate, ev/evita multiple }



