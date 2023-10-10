import os
import fitz
from appendFunctions import *
from findFunctions import *

if __name__ == '__main__':
    files = []
    for file in os.listdir("files"):
        if ".pdf" in file: files.append(file)

    excel = openpyxl.load_workbook(r"excel.xlsx")
    numberRequest = findRequestNumber(excel)
    fileNumber = 1

    for file in files:
        path = "files/" + file
        pdf = fitz.open(path)
        page = pdf.load_page(0)
        text = page.get_text("text")

        address = findAddress(text)
        region = findRegion(address)
        locality = findLocality(address)
        action = "Выписка из ЕГРН"
        date = findRequestDate(text)

        appendInExcel(excel, numberRequest, fileNumber, region, locality, address, action, date)
        fileNumber += 1
        pdf.close()

    excel.save(r"excel.xlsx")
