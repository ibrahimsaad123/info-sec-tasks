def generateADFGVXKeyMatrix(key):
    key = key.upper()
    seen = set()
    matrixList = []
    for ch in key:
        if ch.isalnum() and ch not in seen:
            seen.add(ch)
            matrixList.append(ch)
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if ch not in seen:
            matrixList.append(ch)
    matrix = []
    for i in range(0, 36, 6):
        matrix.append(matrixList[i:i+6])
    return matrix
def adfgvxEnc(plainText, keyMatrix):
    mapping = ['A', 'D', 'F', 'G', 'V', 'X']
    plainText = plainText.upper()
    cipherText = ""
    for ch in plainText:
        if ch.isalnum():
            found = False
            for i in range(6):
                for j in range(6):
                    if keyMatrix[i][j] == ch:
                        cipherText += mapping[i] + mapping[j]
                        found = True
                        break
                if found:
                    break
        else:
            cipherText += ch  
    return cipherText