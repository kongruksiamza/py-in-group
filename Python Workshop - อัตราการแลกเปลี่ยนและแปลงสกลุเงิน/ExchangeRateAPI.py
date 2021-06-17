import requests
import json
response=requests.get('https://api.exchangeratesapi.io/latest')
data=response.text
parsed=json.loads(data)
#print(json.dumps(parsed,indent=4))

date=parsed["date"]
usd_rate=parsed["rates"]["USD"]# rate dollar
thb_rate=parsed["rates"]["THB"]

rates=parsed["rates"]
for currency,rate in rates.items():
    print("1 EUR = ",rate,currency)
    
