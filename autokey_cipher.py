def autokeyEnc(plainText, key):
    key = key.upper()
    keyStream = key + plainText.upper()
    cipherText = ""
    keyIndex = 0
    for ch in plainText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            p = ord(ch.upper()) - ord('A')
            k = ord(keyStream[keyIndex]) - ord('A')
            cipherText += chr((p + k) % 26 + base)
            keyIndex += 1
        else:
            cipherText += ch
    return cipherText
def autokeyDe(cipherText, key):
    key = key.upper()
    plainText = ""
    keyStream = key
    keyIndex = 0
    for ch in cipherText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch.upper()) - ord('A')
            k = ord(keyStream[keyIndex]) - ord('A')
            p = (c - k) % 26
            plainChar = chr(p + ord('A'))
            plainText += chr(p + base)
            keyStream += plainChar
            keyIndex += 1
        else:
            plainText += ch
    return plainText
print(autokeyEnc("HELLO WORLD", 5))