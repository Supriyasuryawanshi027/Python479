import openpyxl

workbook = openpyxl.load_workbook('D:\\pythonProject\\selenium_automation\\Test_data\\Credential.xlsx')
sheet = workbook['Sheet1']
nrows = sheet.max_row
print(nrows)

credentials = []
for row in range(1, nrows+1):
    if row == 1:
        continue
    username = sheet['A'+str(row)].value
    password = sheet['B' + str(row)].value
    expected = sheet['C' + str(row)].value
    credentials.append((username, password, expected))

print(credentials)