import fitz
import docx
import openpyxl.worksheet.worksheet
from findFunctions import findRegion, findPlace, findLocality, findRequestDate
from appendFunctions import appendInExcel, appendInDocx


count = int(input("Количество pdf файлов: "))
excel = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
numberRequest = int(excel['Реестр'][f'A{excel["Реестр"].max_row}'].internal_value.split('/')[0]) + 1

doc = docx.Document()
table = doc.add_table(rows=count, cols=4)
table.style = 'Table Grid'

for iterator in range(1, count + 1):
    fileName = f"{iterator}.pdf"
    pdf = fitz.open(fileName)
    page = pdf.load_page(0)
    text = page.get_text("text")

    address = findPlace(text)
    region = findRegion(address)
    locality = findLocality(address)
    action = "Выписка из ЕГРН"
    date = findRequestDate(text)

    appendInExcel(excel, numberRequest, iterator, region, locality, address, action, date)
    appendInDocx(table, numberRequest, iterator, region, locality, address, date)

excel.save(r"26.05.2023 Реестр по регистрационной работе.xlsx")
doc.save(r"docx.docx")
