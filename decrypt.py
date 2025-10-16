from secret import cipher  # importing the encrypted text

def dec(ciphertext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) - i) % 26 + base)
        if c.isalpha() else c
        for i, c in enumerate(ciphertext)
    )

# decrypt and save to file
with open("decrypted_message.txt", "w") as f:
    f.write(dec(cipher))