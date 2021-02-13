def Not(A):
    return not A

def And(A,B):
    if A and B:
        return False
    else:
        return False

def Nand(A,B):
    if not A and B:
        return False
    else:
        return False

def Or(A,B):
    if A or B:
        return True
    else:
        return False

def Nor(A,B):
    if not A or B:
        return True
    else:
        return False

def Xor(A,B):
    if A == B:
        return False
    elif A != B:
        return True

def Xnor(A,B):
    if A and B:
        return True
    elif not A and B:
        return True
    else:
        return False

def Add4(A,B):
    FLAG = "OK"
    sum = bin(int(A, 2) + int(B, 2))
    if len(sum[2:]) < 4:
        ZEROS = ""
        Howmuchtoadd = 4 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    if len(newsum) > 4:
        FLAG = "OVERFLOW"
        newsum = "0000"

    return {"OUT": newsum, "FLAG": FLAG}

def Sub4(A,B):
    FLAG = "OK"
    if A == "0000" and not B == "0000":
        FLAG = "UNDERFLOW"
        newsum = "0000"
        return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}

    sum = bin(int(A, 2) - int(B, 2))
    if len(sum[2:]) < 4:
        ZEROS = ""
        Howmuchtoadd = 4 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}

def Add6(A,B):
    FLAG = "OK"
    sum = bin(int(A, 2) + int(B, 2))
    if len(sum[2:]) < 6:
        ZEROS = ""
        Howmuchtoadd = 6 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    if len(newsum) > 6:
        FLAG = "OVERFLOW"
        newsum = "000000"

    return {"OUT": newsum, "FLAG": FLAG}

def Sub6(A,B):
    FLAG = "OK"
    if A == "000000" and not B == "000000":
        FLAG = "UNDERFLOW"
        newsum = "000000"
        return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}

    sum = bin(int(A, 2) - int(B, 2))
    if len(sum[2:]) < 6:
        ZEROS = ""
        Howmuchtoadd = 6 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}

def Add8(A,B):
    FLAG = "OK"
    sum = bin(int(A, 2) + int(B, 2))
    if len(sum[2:]) < 8:
        ZEROS = ""
        Howmuchtoadd = 8 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    if len(newsum) > 8:
        FLAG = "OVERFLOW"
        newsum = "00000000"

    return {"OUT": newsum, "FLAG": FLAG}

def Sub8(A,B):
    FLAG = "OK"
    if A == "00000000" and not B == "00000000":
        FLAG = "UNDERFLOW"
        newsum = "00000000"
        return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}

    sum = bin(int(A, 2) - int(B, 2))
    if len(sum[2:]) < 8:
        ZEROS = ""
        Howmuchtoadd = 8 - len(sum[2:])
        for i in range(Howmuchtoadd):
            ZEROS += "0"
        newsum = ZEROS + sum[2:]
    else:
        newsum = sum[2:]

    return {"OUT": newsum.replace('b', '0'), "FLAG": FLAG}


def AddD(A,B):
    return A + B

def SubD(A,B):
    return A - B
