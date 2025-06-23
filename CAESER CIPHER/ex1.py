#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Caesar cipher file encryption/decryption

import argparse

def caesar(text, key, mode):
    result = []

    # Determine shift direction
    if mode == "encrypt":
        shift = key
    elif mode == "decrypt":
        shift = -key
    else:
        return "Invalid mode. Use 'encrypt' or 'decrypt'."

    for char in text:
        if char.isalpha():
            if char.isupper():
                position = ord(char) - ord('A')  # uppercase should use 'A'
                new_position = (position + shift) % 26
                new_char = chr(new_position + ord('A'))
                result.append(new_char)
            elif char.islower():
                position = ord(char) - ord('a')
                new_position = (position + shift) % 26
                new_char = chr(new_position + ord('a'))
                result.append(new_char)
        else:
            result.append(char)

    return "".join(result)

        






def doStuff(filein, fileout, key, mode):
    with open(filein, mode="r", encoding="utf-8", newline="\n") as fin:
        text = fin.read()
        processed = caesar(text, key, mode)
        with open(fileout, mode="w", encoding="utf-8", newline="\n") as fout:
            fout.write(processed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-k", dest="key", type=int, help="key for Caesar cipher")
    parser.add_argument("-m", dest="mode", choices=["encrypt", "decrypt"], help="mode")

    args = parser.parse_args()
    doStuff(args.filein, args.fileout, args.key, args.mode)
