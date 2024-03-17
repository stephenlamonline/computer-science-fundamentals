# testcases:
'''
11
5
0
MATHISCOOL
'''
'''
11
5
1
HFGEPVBDDW
'''
n = 26
m = int(input("m:"))  # y = (ma + k)mod n
k = int(input("k:"))

if input("enter 0 for encryption, 1 for decryption:") == '0':
    # encrypter
    text = list(input("input the text to encrypt:"))
    for i in range(len(text)):
        text[i] = chr((m * (ord(text[i]) - 65) + k) % n + 65)
    print("".join(text))
else:
    # decrypter
    # modular arithmetics, find the inverse of m, then we can decrypt the linear cipher.
    ciphered_text = list(input("input the text to decrypt:"))
    w = 0
    for w in range(n):
        if (w * m) % n == 1:
            break
    for i in range(len(ciphered_text)):
        y = ord(ciphered_text[i]) - 65
        ciphered_text[i] = chr(w * (y - k) % n + 65)
    print("".join(ciphered_text))
