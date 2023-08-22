import fitz
from findFunctions import findRegion, findPlace, findLocality, findRequestDate, findConsiderationDate

count = int(input("Количество pdf файлов: "))
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
