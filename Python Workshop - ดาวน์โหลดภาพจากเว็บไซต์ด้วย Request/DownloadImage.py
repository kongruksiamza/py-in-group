import urllib.request
url=input("แทรกลิงค์สำหรับดาวน์โหลดภาพ :")
name=input("ตั้งชื่อภาพของคุณ:")
#ดาวน์โหลดภาพตามลิงค์ที่ระบุ
urllib.request.urlretrieve(url,"image/"+name+".png")
print("ดาวน์โหลดสมบูรณ์")
