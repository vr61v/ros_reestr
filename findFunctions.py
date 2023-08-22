from Constants import REGIONS
from Constants import LOCALITIES
from Constants import SYMBOLS

def findPlace(text):
    right = 0
    if text.find("Местоположение") != -1:
        right = text.find("Местоположение") + 16
    else:
        right = text.find("Адрес") + 7
    left = text.find("Площадь") - 1
    return text[right:left]

def findRequestDate(text):
    right = text.find("запроса от ") + 11
    return text[right:right + 10]

def findConsiderationDate(text):
    right = text.find("на рассмотрение ") + 16
    return text[right:right + 10]

def findRegion(address):
    index = 0
    for i in REGIONS:
        findIndex = address.find(i)
        if findIndex >= 0:
            index = findIndex
            break

    left = index
    right = index

    while left > 0 and address[left] != ',': left -= 1
    while right < len(address) and address[right] != ',': right += 1
    while address[left] == ',' or address[left] == ' ': left += 1

    region = address[left:right].replace('г.', '')
    if region == "Санкт-Петербург":
        return "СПБ"
    elif region != "Москва":
        newRegion = region[0]
        for i in range(1, len(region)):
            if region[i - 1] == ' ': newRegion += region[i]
        return newRegion.upper()

def findLocality(address):
    index = 0
    indexInLocalities = 0
    locality = ""

    for i in range(len(LOCALITIES)):
        findIndex = address.find(LOCALITIES[i])

        if findIndex >= 0:
            index = findIndex
            indexInLocalities = i

            left = index
            right = index

            while left > 0 and address[left] != ',': left -= 1
            while right < len(address) and address[right] != ',': right += 1
            while address[left] == ',' or address[left] == ' ': left += 1

            flag = False
            for symbol in SYMBOLS:
                if address.find(symbol, left, right) != -1:
                    flag = True

            if flag: continue

            locality = address[left:right]
            break

    if locality.find('.') == -1:
        locality = locality.replace(LOCALITIES[indexInLocalities], LOCALITIES[indexInLocalities + 1])

    return locality