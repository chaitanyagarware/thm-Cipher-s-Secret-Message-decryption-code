# Try-Hack-Me-Cipher-s-Secret-Message-decryption-code
Decryption Script

This project provides a simple decryption algorithm that reverses a position-based Caesar cipher.
It is used to decode text that was previously encoded with the corresponding encryption script.

How It Works

Each letter in the encrypted text is shifted backward by its position in the string.
Non-alphabetic characters, such as numbers or punctuation marks, remain unchanged.

Example:

Encrypted: HFNOS  
Decrypted: HELLO

Files

secret.py – contains the encrypted variable named cipher

cipher = "HFNOS"


decrypt.py – the main script that performs decryption and saves the output

Usage

Clone or download this repository.

Ensure your secret.py file includes the cipher variable.

Run the decryption script:

python3 decrypt.py


The decrypted message will be saved in:

decrypted_message.txt

Logic Summary

Imports the encrypted text from secret.py

Shifts each letter backward based on its position

Preserves uppercase and lowercase letters

Writes the decoded message to decrypted_message.txt

Example
# secret.py
cipher = "HFNOS"

# Output in decrypted_message.txt
HELLO
