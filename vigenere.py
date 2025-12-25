def vigenereEnc(plainText, key):
    key = key.upper()
    cipherText = ""
    keyIndex = 0
    for ch in plainText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            p = ord(ch.upper()) - ord('A')
            k = ord(key[keyIndex % len(key)]) - ord('A')
            cipherText += chr((p + k) % 26 + base)
            keyIndex += 1
        else:
            cipherText += ch
    return cipherText
def vigenereDe(cipherText, key):
    key = key.upper()
    plainText = ""
    keyIndex = 0
    for ch in cipherText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch.upper()) - ord('A')
            k = ord(key[keyIndex % len(key)]) - ord('A')
            plainText += chr((c - k) % 26 + base)
            keyIndex += 1
        else:
            plainText += ch
    return plainText