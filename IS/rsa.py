# text = int(input("Enter number to be ciphered : "))
# p = int(input("Enter P : "))
# q = int(input("Enter Q : "))

# print(f"\nP : {p} & Q : {q}")

# phi_n = (p - 1)*(q - 1)
# n = p*q
# print(f"PHI(N) : {phi_n} & N : {n}")

# def isPrime(ele):
#     for i in range(2, int(ele**(1/2)) + 1):
#         if ele%i == 0:
#             return False
#     return True

# for e in range(n - 1, 2, -1):
#     if e != p and e != q and isPrime(e):
#         break

# for d in range(2, n):
#     if e!=d and (d*e) % phi_n == 1:
#         break

# print(f"Public Key (E) : {(e, n)}")
# print(f"Private Key (D) : {(d, n)}")

# cipher = (text**e)%n
# print(f"\nCipher number : {cipher}")

# decipher = (cipher**d)%n
# print(f"Decipher number : {decipher}")

# Digital
# import hashlib

# p = int(input("Enter P : "))
# q = int(input("Enter Q : "))

# n = p*q
# phi_n = (p - 1)*(q - 1)

# def isPrime(ele):
#     for i in range(2, int(ele**(1/2)) + 1):
#         if ele%i == 0:
#             return False
#     return True

# def encrypt(key, plaintext):
#     d, n = key
#     cipher = plaintext**d % n
#     return cipher

# def decrypt(key, ciphertext):
#     e, n = key
#     decipher = ciphertext**e % n 
#     return decipher

# message = "Hello"
# message_hash = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
# print(f"\nMessage : {message}")
# print(f"Message Digest : {message_hash}")

# for e in range(n-1, 2, -1):
#     if e!=p and e!=q and isPrime(e):
#         break

# d = 3
# while e*d%phi_n != 1:
#     d+=1

# print(f"\nPublic Key : {(e, n)}")
# print(f"Private Key : {(d, n)}")

# signature = encrypt((d, n), message_hash)
# print(f"\nSignature : {signature}")
# print(f"Sender Send (Message, Signature) to Receiver : {(message, signature)}")

# message_hash = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
# print(f"\nHash of message at Receiver : {message_hash}")
# hashfromsignature = decrypt((e, n), signature)
# print(f"Hash from signature : {hashfromsignature}")
# if hashfromsignature == message_hash:
#     print("\nVerifed as both hash matches")
# else:
#     print("\nError")


# 3rd one

# Python Program for implementation of RSA Algorithm

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

# Function to find modular inverse of e modulo phi(n)
# Here we are calculating phi(n) using Hit and Trial Method
# but we can optimize it using Extended Euclidean Algorithm
def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# RSA Key Generation
def generateKeys():
    p = 7919
    q = 1009
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = modInverse(e, phi)

    return e, d, n

# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)

# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)

# Main execution
if __name__ == "__main__":
    
    # Key Generation
    e, d, n = generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    M = 123
    print(f"Original Message: {M}")

    # Encrypt the message
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    # Decrypt the message
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
