from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import sys
ln= dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ID_APP="kongruks-ProductA-PRD-c60bef6c5-325567fb"
api=finding(appid=ID_APP,config_file=None)
keywords=input("Search Keyword Product:")
api_request={'keywords':keywords}
response=api.execute('findItemsByKeywords',api_request)
soup=BeautifulSoup(response.content,'lxml')
total=int(soup.find('totalentries').text)
items=soup.find_all('item')
print("Total = "+str(total))
for item in items:
    title=item.title.string.lower()
    category=item.categoryname.string.lower()
    price=int(round(float(item.currentprice.string)))
    url=item.viewitemurl.string.lower()
    print("-----------------------------------------")
    print("Name = "+title.translate(ln))
    print("Category = "+category)
    print("Price = "+str(price))
    print("Url = "+url)
