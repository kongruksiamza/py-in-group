import folium
m=folium.Map(location=[13.72,100.63],zoom_start=6,tiles='OpenStreet Map')
m.save('thailand.html')
folium.Marker([13.72,100.63],
              popup='<i>กรุงเทพมหานคร</i>',
              tooltip='คลิกที่นี่',
              icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker([14,101],
              popup='<i>นครนายก</i>',
              tooltip='คลิกที่นี่',
              icon=folium.Icon(icon='cloud',color='red')).add_to(m)
folium.Marker([14,100],
              popup='<i>สุพรรณบุรี</i>',
              tooltip='คลิกที่นี่',
              icon=folium.Icon(icon='info-sign',color='green')).add_to(m)
folium.Marker([15,100],
              tooltip='คลิกที่นี่',
              icon=folium.Icon(icon='info-sign',color='blue')).add_to(m)
m.save("Marker.html")
m.add_child(folium.ClickForMarker(popup="Waypoint"))
m.save("GetMarker.html")
m.add_child(folium.LatLngPopup())
m.save("GetLatLng.html")
print("Complete")
