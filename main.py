import fitz


def findPlace(text):
    right = text.find("Местоположение") + 16
    left = text.find("Площадь") - 1
    return text[right:left]
def findRequestDate(text):
    right = text.find("запроса от ") + 11
    return text[right:right + 10]
def findConsiderationDate(text):
    right = text.find("на рассмотрение ") + 16
    return text[right:right + 10]

fileName = "1.pdf"
pdf = fitz.open(fileName)
page = pdf.load_page(0)
text = page.get_text("text")

print(findPlace(text))
print(findRequestDate(text))
print(findConsiderationDate(text))

request = 0  # запрос
region = ""  # регион
locality = ""  # Н. п.
address = ""  # адрес
action = "Выписка из ЕГРН"  # Вид рег. действия
