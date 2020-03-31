import json
import pandas as pd 

stockMonth = pd.read_json('https://cloud.iexapis.com/stable/stock/ba/chart/1m?token=pk_902d6d2f1ce94617bf2e09635fb8974a')
stockMonth.set_index('label', inplace=True)
pd.set_option('display.max_rows', None, 'display.max_columns', None, 'display.width', None)
stockClose = stockMonth[['volume','close']]

print(stockClose)




         












