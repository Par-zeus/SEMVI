import hashlib

def hash_with_sha1(message):
    encoded_msg = message.encode()

    hash_object = hashlib.sha1(encoded_msg)

    hex_dig = hash_object.hexdigest()

    return hex_dig

message = "InformationSecurity123"
hashed_output = hash_with_sha1(message)

print("Original Message:", message)
print("SHA-1 Hashed Output:", hashed_output)
