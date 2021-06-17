import requests
from bs4 import BeautifulSoup
url="https://www.lottery.co.th/small"
data=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})

soup=BeautifulSoup(data.text,'html.parser')

value=soup.find_all("button",{"class":"btn-primary"}) #ปุ่มพร้อมผลหวย 9 button

result=[]

for i in value:
    result.append(i.text) #ดึงเฉพาะข้อความ

print("30 ธันวาคม 62 \n")
print("รางวัลที่ 1 = ",result[0])
print("เลขท้าย 2 ตัว  = ",result[1])
print("เลขหน้า 3 ตัว  = %s ,%s"%(result[2] ,result[3]))
print("เลขท้าย 3 ตัว  = %s ,%s"%(result[4] ,result[5]))