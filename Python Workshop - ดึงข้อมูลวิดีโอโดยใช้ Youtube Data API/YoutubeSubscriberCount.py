import urllib.request
import json
name=input("Input Channel Youtube :")
key="AIzaSyAvDghjpzCjUfxfy9XNjaxH-Ao1WOmzq8I"
data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()

sub=json.loads(data)['items'][0]['statistics']['subscriberCount']
video=json.loads(data)['items'][0]['statistics']['videoCount']
total=json.loads(data)['items'][0]['statistics']['viewCount']

print(name+" ผู้ติดตามช่อง "+"{:,d}".format(int(sub))+" ผู้ติดตาม")                            
print("จำนวนวิดีโอ "+"{:,d}".format(int(video))+" รายการ")  
print("จำนวนการดูทั้งหมด "+"{:,d}".format(int(total))+" วิว")  
