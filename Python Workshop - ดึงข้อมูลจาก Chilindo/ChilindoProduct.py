from bs4 import BeautifulSoup
import requests
import time

def getProduct():
    res=requests.get('https://www.chilindo.com/th/category/650/%E0%B8%AA%E0%B8%B8%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B8%E0%B8%A9')
    soup=BeautifulSoup(res.text,'lxml')
    data=soup.find_all('div',{'class','item-box'})
    for news in data :
        product=news.text.replace(' ','')
        print(product)
    time.sleep(10)
    getProduct()

getProduct()
