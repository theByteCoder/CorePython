import xlrd as xl

try:
    workbook = xl.open_workbook("TestDirectory.xlsx")
    sheet = workbook.sheet_by_index(0)
    for x in range(sheet.nrows):
        if x != 0:
            if sheet.cell(x, 1).value.lower() == "y":
                print(sheet.cell(x, 0).value)
except FileNotFoundError:
    print("File not found")
else:
    print("Executed")
finally:
    print("Completed")
