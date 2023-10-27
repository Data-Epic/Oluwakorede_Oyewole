import gspread
from google.oauth2.service_account import Credentials
import csv
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file('data-epic-project-afa64d8df8db.json', scopes=scopes)


client = gspread.authorize(credentials)
spreadsheet = client.open('Data-Epic-Project-1')
spreadsheet.share("oluwakorede@data-epic-project.iam.gserviceaccount.com", perm_type="user", role="writer")
worksheet = spreadsheet.get_worksheet(0)
worksheet.clear()

with open("concrete.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)


worksheet.update(
    "A1",
    data,
)

