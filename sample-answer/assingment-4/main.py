import random
import sympy
import os


# change the 'bits' variable to a smaller number for better display
# for best security leave it default as 1024
def generate_large_prime(bits=1024):
    while True:
        prime_candidate = sympy.randprime(2 ** (bits - 1), 2 ** bits)
        if sympy.isprime(prime_candidate):
            return prime_candidate


# change the 'bits' variable to a smaller number for better display
# for best security change it to 1024
def generate_keys(bits=10):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537  # Commonly used value for e
    d = sympy.mod_inverse(e, phi_n)
    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)


# (274661, 509189) testing
def main():
    print("Please make sure the files are in the correct directory.")
    print(
        "The message to encrypt should be named \"To-encrypt.txt\", while the file to decrypt should be named "
        "\"encrypted.txt\".")

    mode = input("Enter 'e' for encryption or 'd' for decryption: ")

    if mode == "e":
        public_key, private_key = generate_keys()
        print("Public key:", public_key)
        print("Private key:", private_key)
        message_file = 'To-encrypt.txt'
        with open(message_file, 'r', encoding='utf-8') as f:
            message = f.read()
        ciphertext = encrypt(message, public_key)
        with open('encrypted.txt', 'w') as f:
            f.write(' '.join(map(str, ciphertext)))
        print("Encryption completed. The encrypted file 'encrypted.txt' is created.")

    elif mode == "d":
        d = int(input("Enter the private key (d): "))
        n = int(input("Enter the modulus (n): "))
        private_key = (d, n)
        encrypted_file = 'encrypted.txt'
        with open(encrypted_file, 'r') as f:
            ciphertext = list(map(int, f.read().split()))
        decrypted_message = decrypt(ciphertext, private_key)
        with open('decrypted.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted_message)
        print("Decryption completed. The decrypted file 'decrypted.txt' is created.")


if __name__ == "__main__":
    main()
