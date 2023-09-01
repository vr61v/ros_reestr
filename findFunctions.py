import re
from Constants import REGIONS
from Constants import LOCALITIES
from Constants import LOCALITIES__LEN


def findAddress(text):
    textSplit = text.split(f'\n')
    index = 0

    for i in range(len(textSplit)):
        if textSplit[i].find("Местоположение") >= 0 or textSplit[i].find("Адрес") >= 0:
            index = i + 1
    address = textSplit[index]
    index += 1

    for i in range(index, len(textSplit)):
        if textSplit[i].find("Площадь") >= 0 or textSplit[i] == '2':
            break
        address += ' ' + textSplit[i]

    return address


def findRequestDate(text):
    right = text.find("запроса от ") + 11
    return text[right:right + 10]


def findConsiderationDate(text):
    right = text.find("на рассмотрение ") + 16
    return text[right:right + 10]


def findRegion(address):
    addressSplit = re.split("[:,]", address)
    region = ''

    for i in addressSplit:
        for j in REGIONS:
            if i.find(j) >= 0:
                region = i
                if j == "Москва": return "Москва"
                if j == "Санкт-Петербург": return "СПБ"
                break
        if region != '':
            break

    regionSplit = region.split(' ')
    regionUp = ''
    flag = False
    for i in regionSplit:
        if i == '': continue
        if i.find('обл') >= 0:
            flag = True; continue
        regionUp += i[0].upper()

    if flag: regionUp += 'О'
    return regionUp


def findLocality(address):
    addressSplit = re.split("[:,]", address)
    locality = ""

    for i in addressSplit:
        if len(re.findall("[0-9]", i)) > 0: continue
        if len(re.findall(r"\\/,", i)) > 0: continue

        for j in range(LOCALITIES__LEN):
            index = i.find(LOCALITIES[j])
            if index == -1: continue
            if LOCALITIES[j] == "Москва": return "Москва"
            if LOCALITIES[j] == "Санкт-Петербург": return "СПБ"

            if i[index + len(LOCALITIES[j])] == ' ' or i[index + len(LOCALITIES[j])] == '.':
                if i[0] == ' ': locality = i[1:]
                else: locality = i
                break

        if locality != '':
            break

    return locality
