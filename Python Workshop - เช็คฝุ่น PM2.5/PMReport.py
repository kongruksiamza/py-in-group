import requests
import folium
url="http://air4thai.pcd.go.th/services/getNewAQI_JSON.php"
response=requests.get(url)
data=response.json()

map=folium.Map(location=[13.736,100.523],zoom_start=8)

for item in data["stations"]:
    lat=item['lat']
    lon=item['long']
    level=item['LastUpdate']['AQI']['Level']
    value=int(item['LastUpdate']['AQI']['aqi'])

    color=''
    if(value>=0 and value<=25):
        color='blue'
    elif(value>=26 and value<=50):
        color='green'
    elif(value>=51 and value<=100):
        color='orange'
    elif(value>=101 and value<=200):
        color='red'
    else:
        color='darkpurple'

    folium.Marker([lat,lon],
    tooltip=item['nameTH'],
    popup="AQI:"+str(value)+"\n<i>Level:"+level+"</i>",
    icon=folium.Icon(color=color)
    ).add_to(map)

map.save("index.html")