 
Name: Sarvesh Joaquim Gopu  


This project demonstrates the implementation of the Caesar (Shift) Cipher in Python for both printable text and binary files. The goal is to understand how Caesar Cipher works, test encryption and decryption, and showcase how easily it can be broken via brute-force.

Execution Timestamp:
import datetime  
print("Execution time:", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))

Execution time: 2025-06-26 06:49:13

Part 1: Shift Cipher for Printable Input

Used ex1.py with key 42 to encrypt and decrypt a short Sherlock Holmes text file.

Command to encrypt:
python ex1.py -i sherlock_short.txt -o sherlock_short.en -k 42 -m encrypt

Output of sherlock_short.en:
Ch. Ixuhbesa Xebcui, mxe mqi kikqbbo luho bqju yd jxu cehdydwi, iqlu kfed jxeiu dej ydvhugkudj essqiyedi mxud xu mqi kf qbb dywxj, mqi iuqjut qj jxu rhuqavqij jqrbu.

Command to decrypt:
python ex1.py -i sherlock_short.en -o sherlock_short.dec -k 42 -m decrypt

Output of sherlock_short.dec:
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table.

Part 2: Shift Cipher for Binary Input

Used ex2.py to encrypt and decrypt binary content with the same key.

Command to encrypt:
python ex2.py -i sherlock_short.txt -o sherlock_short.en.bin -k 42 -m encrypt

Output (binary, unreadable):
w�XJ}�������Jr�����VJ���J���J�������J����J����J��J���J��������VJ����J����J�����J���J����������J���������J����J��J���J��J���J�����VJ���J������J��J���J���������J�����X

Command to decrypt:
python ex2.py -i sherlock_short.en.bin -o sherlock_short.de.txt -k 42 -m decrypt

Output of sherlock_short.de.txt:
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table.

Part 3: Break Shift Cipher of Flag

Checked the file:
file flag

Output:
flag: data

Ran brute-force breaker to find key and decrypt:
python ex2.py -i flag -o flag_decrypted.png

Output:
Found key=246. Decrypted PNG written to flag_decrypted.png

Displayed the image using Python:

from PIL import Image  
import os  
os.system("python ex2.py -i flag -o flag_decrypted.png")  
img = Image.open("flag_decrypted.png")  
img.show()

The image was correctly displayed, confirming successful brute-force decryption.

This lab demonstrated the working of the Caesar cipher on both text and binary files. It also showed how easy it is to break Caesar cipher via brute force, especially for binary data, as the key space is only 256. We encrypted and decrypted files with a known key, and then successfully recovered a PNG image from an encrypted binary by brute-forcing the key.

Tools used:  
- Python 3  
- argparse  
- PIL (Pillow)  
- file I/O  
- terminal commands

End of report.
