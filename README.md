🔐 Caesar Cipher Encryption and Brute-force Decryption 
This project demonstrates the use of the Caesar (Shift) Cipher to encrypt and decrypt both text and binary files. It also showcases how Caesar Cipher can be broken using brute-force, highlighting its weaknesses in real-world applications. This lab was completed using Python with a custom-built cipher script.
 
Name: Sarvesh Joaquim Gopu  


🗂️ Project Files  
ex1.py – Caesar cipher for printable (text) input  
ex2.py – Caesar cipher for binary input  
sherlock_short.txt – Sample text input  
flag – Encrypted binary image  
flag_decrypted.png – Final output image after successful decryption  

🧪 Lab Execution Time  
import datetime  
print("Execution time:", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))  
Execution time: 2025-06-26 06:49:13  

🔤 Part 1: Printable Text Encryption and Decryption  
Tool: ex1.py  
Key Used: 42  

Encrypt:  
python ex1.py -i sherlock_short.txt -o sherlock_short.en -k 42 -m encrypt  

Encrypted Output:  
Ch. Ixuhbesa Xebcui, mxe mqi kikqbbo luho bqju yd jxu cehdydwi, iqlu kfed jxeiu dej ydvhugkudj essqiyedi mxud xu mqi kf qbb dywxj, mqi iuqjut qj jxu rhuqavqij jqrbu.  

Decrypt:  
python ex1.py -i sherlock_short.en -o sherlock_short.dec -k 42 -m decrypt  

Decrypted Output:  
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table.  

💾 Part 2: Binary File Encryption and Decryption  
Tool: ex2.py  
Key Used: 42  

Encrypt:  
python ex2.py -i sherlock_short.txt -o sherlock_short.en.bin -k 42 -m encrypt  

Binary Output (unreadable characters):  
w�XJ}�������Jr�����VJ���J���J...  

Decrypt:  
python ex2.py -i sherlock_short.en.bin -o sherlock_short.de.txt -k 42 -m decrypt  

Decrypted Output:  
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table.  

🧠 Part 3: Brute-force Decryption of Encrypted Image  
Used brute-force to discover Caesar key and decrypt a binary file (`flag`) into a PNG image.  

Check file type:  
file flag  
Output: flag: data  

Run Brute-force:  
python ex2.py -i flag -o flag_decrypted.png  
Output: Found key=246. Decrypted PNG written to flag_decrypted.png  

🖼️ View the Decrypted Image  
from PIL import Image  
import os  
os.system("python ex2.py -i flag -o flag_decrypted.png")  
img = Image.open("flag_decrypted.png")  
img.show()  

✅ The image was correctly displayed, confirming successful brute-force decryption.  

📌 Key Learnings  
- Applied Caesar Cipher on both text and binary data  
- Validated encryption/decryption using custom Python tools  
- Demonstrated how Caesar Cipher can be brute-forced easily  
- Successfully decrypted a binary image by guessing the correct Caesar shift  

🛠️ Technologies Used  
- Python 3  
- argparse  
- PIL (Pillow)  
- Terminal utilities (`file`, `os`)  
- No external crypto libraries used  

🚀 How to Run  
1. Ensure `ex1.py`, `ex2.py`, and all input files are in the same directory  
2. Run the encryption or decryption commands as shown above  
3. Use brute-force (with ex2.py) to break unknown Caesar keys on binary files  
4. Use PIL to open any decrypted image output  

📎 End of Lab Report  
