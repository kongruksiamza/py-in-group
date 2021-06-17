import yweather
from weather import Weather,Unit
client=yweather.Client()
name=input("Input Your City :")
dataid=client.fetch_woeid(name+",Thailand")
weather=Weather(unit=Unit.CELSIUS)
lookup=weather.lookup(dataid)
condition=lookup.condition

location=weather.lookup_by_location(name+",Thailand")
forcasts=location.forecast
for result in forcasts:
    print("สภาพอากาศ : "+result.text)
    print("วันที่ : "+result.date)
    print("อุณหภูมิสูงสุด : "+result.high)
    print("อุณหภูมิต่ำสุด : "+result.low)
    print("-------------------")
