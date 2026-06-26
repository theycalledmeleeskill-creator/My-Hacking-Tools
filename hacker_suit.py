import subprocess
from cryptography.fernet import Fernet
print("---Lauching Hacker Suit---")
result=subprocess.run(["whoami"],capture_output=True,text=True)
username=result.stdout.strip()
with open("viction_info.txt","w")as f:
	f.write(f"[+] Compromised User : {username}")
key=Fernet.generate_key()
cipher=Fernet(key)
with open("viction_info.txt","rb")as f:
	original_data=f.read()
encrypted_data=cipher.encrypt(original_data)
with open("viction_info.txt","wb")as f:
	f.write(encrypted_data)
print(f"[+] File encrypted successfully!")
print(f"[!] Keep this Key to decrypt later: {key.decode()}")
