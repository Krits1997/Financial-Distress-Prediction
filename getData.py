import pandas as pd
import requests
import json

df = pd.read_excel('Tickers.xlsx')
Companies = pd.DataFrame()

for i in df['Ticker names']:
  apiPath = 'https://financialmodelingprep.com/api/v3/ratios/'+str(i)+'?apikey=68aff3a70cc7e28159a88646ab58c6d0'
  finInfo = requests.get(apiPath)
  if(finInfo.json()):
    print(finInfo.json())
    data = finInfo.json()[0]
    print(data)
    Companies = Companies.append(pd.json_normalize(data), ignore_index = True)


print(Companies)
writer = pd.ExcelWriter('FinRatios.xlsx')
Companies.to_excel(writer,'CompanyInfo')
writer.save()