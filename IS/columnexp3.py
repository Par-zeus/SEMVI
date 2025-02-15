import math
import random

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()

def encryptMessage(msg, key):
    cipher = ""
    msg = msg.replace(" ", "")  # Remove spaces from the message

    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key = key.upper()
    key_lst = sorted(list(key))

    col = len(key)
    row = int(math.ceil(msg_len / col))

    # Add random padding letters if needed
    fill_null = int((row * col) - msg_len)
    if fill_null > 0:
        padding = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(fill_null)]
        msg_lst.extend(padding)

    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    print(f"Encryption Matrix (Key: {key}):")
    display_matrix(matrix)

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def decryptMessage(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_lst = list(cipher)
    key = key.upper()
    col = len(key)
    row = int(math.ceil(len(cipher) / col))
    key_lst = sorted(list(key))

    dec_cipher = [[None] * col for _ in range(row)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            if msg_indx < len(msg_lst):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
        k_indx += 1

    print(f"Decryption Matrix (Key: {key}):")
    display_matrix(dec_cipher)
    msg = ''.join(sum(dec_cipher, []))

    return msg

# Main execution
msg = input("Enter the message: ").replace(" ", "")
transpositions = int(input("Number of transpositions: "))
keys = [input(f"Key {i+1}: ").upper() for i in range(transpositions)]

# Encrypt multiple times
cipher = msg
for key in keys:
    cipher = encryptMessage(cipher, key)
print("Final Cipher:", cipher)

# Decrypt multiple times (reverse order)
decrypted = cipher
for key in reversed(keys):
    decrypted = decryptMessage(decrypted, key)
print("Decrypted Message:", decrypted)