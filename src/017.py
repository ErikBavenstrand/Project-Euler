singleDigit = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 'hundred'
thousand = 'thousand'
andWord = 'and'

def numberInLetters(number):
    if number > 1000:
        return EnvironmentError
    isTens = False
    isHundred = False
    isThousand = False
    if number % 10 == 0:
        isTens = True
    if number % 100 == 0:
        isHundred = True
    if number % 1000 == 0:
        isThousand = True
    returnString = ''
    numberDivided = list(str(number))
    lenghtOfNumber = len(numberDivided)

    if lenghtOfNumber > 3:
        returnString += (singleDigit[int(numberDivided[0])] + thousand)
        return returnString
        numberDivided.remove(numberDivided[0])
        lenghtOfNumber -= 1
        if isThousand == True:
            return returnString
    if lenghtOfNumber > 2:
        returnString += (singleDigit[int(numberDivided[0])] + hundred)
        numberDivided.remove(numberDivided[0])
        lenghtOfNumber -= 1
        if isHundred == True:
            return returnString
        returnString += andWord
    if lenghtOfNumber > 1:
        tensNumber = int(numberDivided[0] + numberDivided[1])
        if tensNumber < 20 and tensNumber > 10:
            returnString += teens[int(numberDivided[1])]
            return returnString
        elif isTens == True:
            returnString += tens[int(numberDivided[0])]
            return returnString
        elif tensNumber >= 10:
            returnString += tens[int(numberDivided[0])]
        numberDivided.remove(numberDivided[0])
        lenghtOfNumber -= 1
    if lenghtOfNumber > 0:
        returnString += singleDigit[int(numberDivided[0])]
        return returnString
length = 0
for i in range(1, 1001):
    length += len(numberInLetters(i))
print(length)