import requests
import json
base=input("แปลงจากสกุลเงิน :")
to=input("เป็นสกุลเงิน :")
amount=float(input("จำนวนเงิน :"))

url="https://api.exchangeratesapi.io/latest?base="+base
response=requests.get(url)
data=response.text
parsed=json.loads(data)
rates=parsed["rates"]

for currency,rate in rates.items():
    if currency == to:
        conversion=rate*amount # คำนวณหาจำนวนเงิน
        print("1",base,"=",currency,rate)
        print(amount,base,"=",currency,conversion)
