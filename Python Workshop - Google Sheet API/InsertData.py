import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('GoogleDemo.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open("Customer").sheet1

#บันทึกข้อมูล
row = ["kongruksiam","300"]
sheet.insert_row(row, 24)

pp=pprint.PrettyPrinter()
result=sheet.get_all_records()
pp.pprint(result)

#อัพเดทข้อมูล
sheet.update_cell(23,2,'3000')

