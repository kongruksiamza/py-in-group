from googletrans import Translator

translator=Translator()
message=input("ป้อนข้อความที่ต้องการแปล = ")

result=translator.translate(message,dest='en')

print("ภาษาไทย = " ,result.origin, " ภาษาอังกฤษ = " ,result.text)