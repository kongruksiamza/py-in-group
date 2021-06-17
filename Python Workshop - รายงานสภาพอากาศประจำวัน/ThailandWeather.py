import requests
from bs4 import BeautifulSoup

url="https://www.tmd.go.th/climate/climate.php?FileID=1" 
data=requests.get(url)
soup=BeautifulSoup(data.text,'html.parser')
cityrow=soup.find_all("tr",{"class":"RDS"})

my_city=[]
for col in cityrow:
    citycol=col.find_all("td")
    for singlecol in citycol:
        my_city.append(singlecol.text)

result=my_city.index(input("ป้อนชื่อจังหวัด = "))
print("อุณหภูมิสูงสุด = "+my_city[result+1])
print("อุณหภูมิต่ำสุด = "+my_city[result+2])
print("ทิศทาง = "+my_city[result+3])
print("ความเร็วลม = "+my_city[result+4]+" กม/ซม")
print("เวลา = "+my_city[result+5])
print("ปริมาณน้ำฝน = "+my_city[result+6])
print("รวมทั้งปี= "+my_city[result+7])