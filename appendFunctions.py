import openpyxl.worksheet.worksheet
from openpyxl.styles import Alignment

def appendInExcel(excel, numberRequest, iterator, region, locality, address, action, date):
    page = excel['Реестр']
    max_row = page.max_row + 1
    page.append({'A': f"{numberRequest}/{iterator}", 'B': f"{region}", 'C': f"{locality}",
                 'D': f"{address}", 'E': f"{action}", 'G': f"{date}", 'H': f"{date}",
                 'I': f"{date}", 'N': f"{date}"})

    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']:
        page[f'{letter}{max_row}'].alignment = Alignment(wrapText=True)
    for letter in ['G', 'H', 'I', 'N']:
        page[f'{letter}{max_row}'].number_format = openpyxl.styles.numbers.BUILTIN_FORMATS[15]
        page[f'{letter}{max_row}'].alignment = Alignment(horizontal="right")


def appendInDocx(table, numberRequest, iterator, region, locality, address, date):
    cells = table.rows[iterator - 1].cells
    cells[0].text = "0"
    cells[1].text = f"{region}, {locality}, {address}(Запрос №{numberRequest}/{iterator} от {date}"
    cells[2].text = "1- ЕГРН"
    cells[3].text = "500"
    return 0
