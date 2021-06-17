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
pp.pprint(result)
