import fitz
import openpyxl.worksheet.worksheet
from appendFunctions import appendInExcel
from findFunctions import findRegion, findAddress, findLocality, findRequestDate


count = int(input("Количество pdf файлов: "))
excel = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
numberRequest = int(excel['Реестр'][f'A{excel["Реестр"].max_row}'].internal_value.split('/')[0]) + 1

for iterator in range(1, count + 1):
    fileName = f"файл {iterator}.pdf"
    pdf = fitz.open(fileName)
    page = pdf.load_page(0)
    text = page.get_text("text")

    address = findAddress(text)
    region = findRegion(address)
    locality = findLocality(address)
    action = "Выписка из ЕГРН"
    date = findRequestDate(text)

    appendInExcel(excel, numberRequest, iterator, region, locality, address, action, date)

excel.save(r"26.05.2023 Реестр по регистрационной работе.xlsx")
