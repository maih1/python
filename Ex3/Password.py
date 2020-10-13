def checkLen(s):
    return len(s) >= 8 and len(s) <= 100

def checkUpper(s):
    for i in s:
        if i.isupper():
            return True
    return False

def checkLower(s):
    for i in s:
        if i.islower():
            return True
    return False


def checkDigit(s):
    for i in s:
        if i.isdigit():
            return True
    return False

def checkSymbol(s):
    symbol = "~!@#$%^&*"
    for i in symbol:
        if i in s:
            return True
    return False

def checkPassword(s):
    if(checkLen(s) == True and checkLower(s) == True and checkUpper(s) == True and checkSymbol(s) == True and checkDigit(s) == True):
        return True
    return False