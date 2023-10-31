import os

from PyPDF2 import PdfReader
from appendFunctions import *
from findFunctions import *

files = []
for file in os.listdir("files"):
    if ".pdf" in file: files.append(file)

excel = openpyxl.load_workbook(r"excel.xlsx")
numberRequest = findRequestNumber(excel)
fileNumber = 1

for file in files:
    try:
        path = "files/" + file
        pdf = PdfReader(path)
        page = pdf.pages[0]
        text = page.extract_text("text")

        address = findAddress(text)
        region = findRegion(address)
        locality = findLocality(address)
        action = "Выписка из ЕГРН"
        date = findRequestDate(text)

        appendInExcel(excel, numberRequest, fileNumber, region, locality, address, action, date)
        fileNumber += 1
    except:
        print(Exception)

excel.save(r"excel1.xlsx")
