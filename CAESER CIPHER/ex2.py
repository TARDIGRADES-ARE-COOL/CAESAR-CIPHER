#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Byte-level Caesar cipher with brute-force break for PNG

import argparse
import sys

# Byte-wise Caesar encryption/decryption
def caesar_bytes(data: bytes, key: int, mode: str) -> bytes:
    if mode == "encrypt":
        shift = key
    elif mode == "decrypt":
        shift = -key
    else:
        # treat any other mode as 'break' when decrypting
        shift = -key
    return bytes((byte + shift) % 256 for byte in data)


def doStuff(filein: str, fileout: str, key: int, mode: str) -> None:
    with open(filein, "rb") as fin:
        binary_data = fin.read()
    processed = caesar_bytes(binary_data, key, mode)
    with open(fileout, "wb") as fout:
        fout.write(processed)


def break_png(filein: str, fileout: str) -> None:
    """
    Brute-force decrypt keys 0–255, detect PNG signature, write out plaintext PNG.
    """
    PNG_SIG = b"\x89PNG\r\n\x1a\n"
    try:
        data = open(filein, 'rb').read()
    except IOError as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    for key in range(256):
        decrypted = caesar_bytes(data, key, "decrypt")
        if decrypted.startswith(PNG_SIG):
            try:
                with open(fileout, 'wb') as fout:
                    fout.write(decrypted)
                print(f"Found key={key}. Decrypted PNG written to {fileout}")
            except IOError as e:
                print(f"Error writing output file: {e}", file=sys.stderr)
                sys.exit(1)
            sys.exit(0)

    print("Failed to recover a valid PNG with any key 0-255.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Byte-level Caesar cipher: encrypt, decrypt, or break (PNG only)'
    )
    parser.add_argument("-i", dest="filein", required=True, help="input file")
    parser.add_argument("-o", dest="fileout", required=True, help="output file")
    parser.add_argument("-k", dest="key", type=int,
                        help="key for byte Caesar cipher (required for encrypt/decrypt)")
    parser.add_argument(
        "-m", dest="mode",
        choices=["encrypt", "decrypt", "break"],
        default="break",
        help="mode: encrypt, decrypt, or break (PNG). Default is break when not specified."
    )

    args = parser.parse_args()
    if args.mode == "encrypt" or args.mode == "decrypt":
        if args.key is None:
            parser.error("-k/--key is required for encrypt/decrypt modes.")
        doStuff(args.filein, args.fileout, args.key, args.mode)
    else:
        # break mode (default)
        break_png(args.filein, args.fileout)
