import smtplib
import Config

recipient=input("ป้อนอีเมลผู้รับ : ")
subject=input("หัวข้อที่ส่ง : ")
content=input("เนื้อหา : ")
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(Config.email,Config.password)

#content="Hello Python" ตัวอย่างตามคลิป
#subject="Test Python" ตัวอย่างตามคลิป

email_text="""
From:%s
To:%s
Subject:%s
%s
"""%(Config.email,recipient,subject,content)


#กำหนดส่วน Header และรองรับการส่งข้อมูลภาษาไทย
message = 'Subject: {}\n\n{}'.format(subject,email_text).encode('utf-8')

server.sendmail(Config.email,recipient,message)
server.quit()
print("Send Complete")
