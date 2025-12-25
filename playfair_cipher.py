def processPlainText(text):
    text = text.upper()
    text = text.replace("J", "I")
    processed = ""
    for ch in text:
        if ch.isalpha():
            processed += ch
    digraphs = []
    i = 0
    while i < len(processed):
        if i + 1 < len(processed):
            if processed[i] == processed[i + 1]:
                digraphs.append(processed[i] + 'X')
                i += 1
            else:
                digraphs.append(processed[i] + processed[i + 1])
                i += 2
        else:
            digraphs.append(processed[i] + 'X')
            i += 1
    return digraphs
def generateKeyMatrix(key):
    key = key.upper()
    key = key.replace("J", "I")
    seen = set()
    matrixList = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrixList.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            matrixList.append(ch)
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(matrixList[i:i+5])
    return matrix