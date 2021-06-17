import time
from datetime import datetime as dt

#host file
host_path="C:\Windows\System32\drivers\etc\hosts"
websites=["www.youtube.com","https://www.youtube.com","www.google.com","https://www.google.com"]

redirect="127.0.0.1"

#การตั้งเวลา
starttime=dt(dt.now().year,dt.now().month,dt.now().day,5)
endtime=dt(dt.now().year,dt.now().month,dt.now().day,10)

currenttime=dt.now()

while True:
    if(starttime<currenttime<endtime):
        print("block")
        with open(host_path,"r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)

