import hashlib

# ---------- Step 1: SHA-1 Hash ----------
def hash_with_sha1(message):
    encoded_msg = message.encode()
    hash_object = hashlib.sha1(encoded_msg)
    hex_dig = hash_object.hexdigest()
    return hex_dig

# ---------- Step 2: RSA Keys (Small, for demo only) ----------
n = 3233
e = 17
d = 2753

# ---------- Step 3: Sign Function ----------
def sign_from_hash(hex_hash):
    hash_int = int(hex_hash, 16) % n  # MODULO to fit in range of n
    signature = pow(hash_int, d, n)
    return signature, hash_int  # returning both for verification

# ---------- Step 4: Verify Function ----------
def verify_from_hash(hash_int, signature):
    decrypted = pow(signature, e, n)
    return hash_int == decrypted

# ---------- Step 5: Run ----------
message = "InformationSecurity123"
hex_hash = hash_with_sha1(message)

signature, reduced_hash = sign_from_hash(hex_hash)

print("Original Message:", message)
print("SHA-1 Hash:", hex_hash)
print("Reduced Hash (mod n):", reduced_hash)
print("RSA Signature:", signature)

# Verify
if verify_from_hash(reduced_hash, signature):
    print("✅ Signature is valid!")
else:
    print("❌ Signature is invalid.")
