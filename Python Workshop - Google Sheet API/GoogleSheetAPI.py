#pip install gspread oauth2client
#pip install pprint
#https://gspread.readthedocs.io/en/latest/oauth2.html#oauth-credentials
#https://console.developers.google.com/apis/dashboard

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('GoogleDemo.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open("Customer").sheet1

pp=pprint.PrettyPrinter()
result=sheet.get_all_records()
value=sheet.acell('A1').value
value_col=sheet.col_values(1)
value_row=sheet.row_values(1)

#ค้นหาข้อมูล
cell=sheet.findall("150")
#for result in cell:
 #   pp.pprint("เจอข้อมูลที่ตำแหน่ง R%sC%s"%(result.row,result.col))

#อัพเดทข้อมูล
sheet.update_cell(23,2,'1000')

#row = ["kongruksiam","300"]
#sheet.insert_row(row, 24)
sheet.delete_row(24)

