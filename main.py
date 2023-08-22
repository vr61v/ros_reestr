import fitz
from openpyxl import load_workbook
import openpyxl.worksheet.worksheet
from openpyxl.styles import Alignment

from findFunctions import findRegion, findPlace, findLocality, findRequestDate, findConsiderationDate


def countRequest():
    excel = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
    page = excel['Реестр']
    return int(page[f'A{page.max_row}'].internal_value.split('/')[0]) + 1


count = int(input("Количество pdf файлов: "))
numberRequest = countRequest()

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

    excel = openpyxl.load_workbook(r"26.05.2023 Реестр по регистрационной работе.xlsx")
    page = excel['Реестр']
    max_row = page.max_row + 1

    page.append({'A': f"{numberRequest}/{iterator}", 'B': f"{region}", 'C': f"{locality}",
                 'D': f"{address}", 'E': f"{action}", 'G': f"{date}", 'H': f"{date}",
                 'I': f"{date}", 'N': f"{date}"})

    for letter in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']:
        page[f'{letter}{max_row}'].alignment = Alignment(wrapText=True)
    for letter in ['G','H','I','N']:
        page[f'{letter}{max_row}'].number_format = openpyxl.styles.numbers.BUILTIN_FORMATS[15]
        page[f'{letter}{max_row}'].alignment = Alignment(horizontal="right")

    excel.save(r"26.05.2023 Реестр по регистрационной работе.xlsx")
