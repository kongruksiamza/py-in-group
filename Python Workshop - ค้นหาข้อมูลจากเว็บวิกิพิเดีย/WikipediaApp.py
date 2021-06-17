import wikipedia
message=input("ค้นหาบทความที่ต้องการ : ")
wikipedia.set_lang('th')
result=wikipedia.summary(message,sentences=1)
print(result)
