import openpyxl
import os

path = os.getcwd()
print(path)
wb = openpyxl.load_workbook(path + "/ExcelFiles/AllReports2.xlsx")

wb.save("Sample.pdf")
