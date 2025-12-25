def multiplicativeEnc(plainText, key):
    if key % 2 == 0 or key % 13 == 0:
        raise ValueError("Key must be coprime with 26")
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            cipherText += chr((c * key) % 26 + base)
        else:
            cipherText += ch
    return cipherText
def modInverse(key, mod=26):
    for i in range(1, mod):
        if (key * i) % mod == 1:
            return i
    return None
def multiplicativeDe(cipherText, key):
    invKey = modInverse(key)
    if invKey is None:
        raise ValueError("Key has no modular inverse")
    plainText = ""
    for ch in cipherText:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            plainText += chr((c * invKey) % 26 + base)
        else:
            plainText += ch
    return plainText
def bruteForceMultiplicative(cipherText):
    valid_keys = [1,3,5,7,9,11,15,17,19,21,23,25]
    results = []
    for key in valid_keys:
        invKey = modInverse(key)
        decrypted = ""
        for ch in cipherText:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                c = ord(ch) - base
                decrypted += chr((c * invKey) % 26 + base)
            else:
                decrypted += ch
        results.append((key, decrypted))
    return results


