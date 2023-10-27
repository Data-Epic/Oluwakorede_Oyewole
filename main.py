import gspread
from google.oauth2.service_account import Credentials
import csv
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Google api credential
google_json_file = input("Enter the google credential json file")
credentials = Credentials.from_service_account_file(google_json_file, scopes=scopes)

spreadsheet_name = input("Enter your spreadsheet name")

client = gspread.authorize(credentials)
spreadsheet = client.open(spreadsheet_name)
spreadsheet.share("oluwakorede@data-epic-project.iam.gserviceaccount.com", perm_type="user", role="writer")
worksheet_name = input("Enter a worksheet name")
ncolumns = input("Enter the number of columns")
nrows = input("Enter the number of nrows")

worksheet = spreadsheet.add_worksheet(title=worksheet_name,rows=nrows, cols=ncolumns)
worksheet.clear()

filename = input("Enter a filename")

with open(filename, "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)


worksheet.update(
    "A1",
    data,
)

