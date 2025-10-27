import re

def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    checkSum = 0
    reverse_digits = string[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        checkSum += n
    return checkSum

def getCardType(string):
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r'^5[1-5]', string):
        return "Master Card"
    return "Invalid"

cardNumber = input("Введите номер банковской карты: ")
if isValidNumber(cardNumber):
    if getCheckSum(cardNumber) % 10 == 0:
        print(getCardType(cardNumber))
    else:
        print("Неверная контрольная сумма")
else:
    print("Неверный формат номера")
