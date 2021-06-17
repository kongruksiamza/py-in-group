from zeep import Client
import xml.etree.ElementTree as ET
url="https://www.pttor.com/OilPrice.asmx?wsdl"
client_api = Client(url)
result=client_api.service.CurrentOilPrice("en")

e=ET.ElementTree(ET.fromstring(result))
for elt in e.iter():
    print(elt.text)