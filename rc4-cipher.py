def rc4_key_stream(key, n):
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]   
    i = 0
    j = 0
    keystream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]   
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream
def binary_derivative_test(bits):
    derivative = ""
    for i in range(len(bits) - 1):
        derivative += str(int(bits[i]) ^ int(bits[i + 1]))
    ones = derivative.count('1')
    zeros = derivative.count('0')
    return ones, zeros
def change_point_test(bits):
    n = len(bits)
    mean = bits.count('1') / n
    max_diff = 0
    change_point = 0
    for i in range(1, n):
        left_mean = bits[:i].count('1') / i
        right_mean = bits[i:].count('1') / (n - i)
        diff = abs(left_mean - right_mean)
        if diff > max_diff:
            max_diff = diff
            change_point = i
    return change_point, max_diff
if __name__ == "__main__":
    key = "SECRET"
    n = 32   
    keystream = rc4_key_stream(key, n)
    bits = ''.join(format(b, '08b') for b in keystream)
    print("Keystream:", keystream)
    print("Binary string:", bits)
    ones, zeros = binary_derivative_test(bits)
    print("Binary Derivative Test -> Ones:", ones, "Zeros:", zeros)
    cp, diff = change_point_test(bits)
    print("Change Point:", cp, "Max Difference:", diff)