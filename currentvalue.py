import pandas as pd
from urllib.request import Request, urlopen

class CurVal():

    def __init__(self, ticker) -> None:
        self.ticker = ticker

    def getcurval(self):
        reqShare = Request(url='https://stockanalysis.com/stocks/{}/'.format(self.ticker), headers={'User-Agent': 'Mozilla/5.0'})
        sharetable = pd.read_html(urlopen(reqShare).read(), index_col = 0)[1]

        return float(sharetable[1]['Open'])