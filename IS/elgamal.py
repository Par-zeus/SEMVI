import random
import hashlib

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def hash_message(message):
    hash_object = hashlib.sha1(message.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

# Key Generation
def generate_keys(p, g):
    x = random.randint(1, p-2)         # Private key
    y = pow(g, x, p)                   # Public key
    return x, y

def sign(message, p, g, x):
    H = hash_message(message)
    while True:
        k = random.randint(1, p-2)
        if gcd(k, p-1) == 1:
            break
    r = pow(g, k, p)
    k_inv = modinv(k, p-1)
    s = (k_inv * (H - x * r)) % (p - 1)
    return r, s

def verify(message, r, s, p, g, y):
    if not (0 < r < p):
        return False
    H = hash_message(message)
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, H, p)
    return v1 == v2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

p = 467        # Prime number
g = 2          # Generator
message = "InformationSecurity123"
    
x, y = generate_keys(p, g)
print("Private key x:", x)
print("Public key y:", y)

r, s = sign(message, p, g, x)
print("\nSignature (r, s):", r, s)

is_valid = verify(message, r, s, p, g, y)
print("\n✅ Signature is valid!" if is_valid else "❌ Signature is invalid.")
