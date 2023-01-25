import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import Request, urlopen

y2021 = {}
y2020 = {}
y2019 = {}
y2018 = {}
y2017 = {}
businessvalue = {}

EBITDA = [0,0,0,0,0]
FCF = [0,0,0,0,0]

# tickername = input()
tickername = 'tsla'


# driver = webdriver.Chrome(DRIVER_PATH)
# driver.get("https://stockanalysis.com/stocks/{}/".format(tickername))
# time.sleep(3)
# driver.get("https://stockanalysis.com/stocks/{}/financials/".format(tickername))


req = Request(url='https://stockanalysis.com/stocks/{}/financials/'.format(tickername), headers={'User-Agent' : 'Mozilla/5.0'})
webpage = urlopen(req).read()

table_MN = pd.read_html(webpage)
#print(f'Total tables: {len(table_MN)}')


table_MN = pd.read_html(webpage, match='Revenue')

print(table_MN[0]['2021'][0:9])   #EBITDA (NEED)
                                    #->YOY Change, AVG EBITA GROWTH
                                  #Past Free Cash Flow (NEED)
                                    #->YOY Change, AVG Past Free Cashflow
                                  #NOT ON THE WEBSITE
                                    #Assumptions {EBITDA growth rate, free cash flow rate, rate of return, terminal growth rate, ev/evita multiple }



