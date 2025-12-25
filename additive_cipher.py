def additiveEnc(plainText, key):
    cipherText = ""
    if isinstance(key,str):
      keyAsNumber = ord(key.upper()) - ord('A')
    elif isinstance(key, int):
        keyAsNumber = key
    else:
        raise ValueError("key must be int or string")
    for ch in plainText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            sumAsNum = (c + keyAsNumber) % 26
            cipherText += chr(sumAsNum + base)
        else:
            cipherText += ch
    return cipherText
def additiveDe(cipherText, key):
    plaintext = ""
    if isinstance(key, str):
        keyAsNumber = ord(key.upper()) - ord('A')
    elif isinstance(key, int):
        keyAsNumber = key
    else:
        raise ValueError("key must be int or string")
    for ch in cipherText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            sumAsNum = (c - keyAsNumber) % 26
            plaintext += chr(sumAsNum + base)
        else:
            plaintext += ch
    return plaintext
def bruteForceAdditive(cipherText):
    possible_texts = []
    for key in range(26):
        decrypted = ""
        for ch in cipherText:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                c = ord(ch) - base
                decrypted += chr((c - key) % 26 + base)
            else:
                decrypted += ch
        possible_texts.append((key, decrypted))
    return possible_texts

