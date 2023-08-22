import fitz
from openpyxl import load_workbook
import openpyxl.worksheet.worksheet
from findFunctions import findRegion, findPlace, findLocality, findRequestDate, findConsiderationDate

count = int(input("Количество pdf файлов: "))

excel = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
page = excel['Реестр']
numberRequest = int(page[f'A{page.max_row}'].internal_value.split('/')[0]) + 1

for iterator in range(1, count + 1):
    fileName = f"{iterator}.pdf"
    pdf = fitz.open(fileName)
    page = pdf.load_page(0)
    text = page.get_text("text")

    address = findPlace(text)
    region = findRegion(address)
    locality = findLocality(address)
    action = "Выписка из ЕГРН"
    requestDate = findRequestDate(text)
    considerationDate = findConsiderationDate(text)

    excel2 = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
    page2 = excel2['Реестр']
    max_row = page2.max_row + 1
    page2[f'A{max_row}'] = f"{numberRequest}/{iterator}"
    page2[f'B{max_row}'] = f"{region}"
    page2[f'C{max_row}'] = f"{locality}"
    page2[f'D{max_row}'] = f"{address}"
    page2[f'F{max_row}'] = f"{action}"
    page2[f'G{max_row}'] = f"{requestDate}"
    page2[f'H{max_row}'] = f"{requestDate}"
    page2[f'I{max_row}'] = f"{considerationDate}"

    excel2.save(r"26.05.2023 Реестр по регистрационной работе.xlsx")
