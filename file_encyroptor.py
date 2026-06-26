from cryptography.fernet import Fernet
print("[*]Target file encryption process started...")
key=Fernet.generate_key()
cipher=Fernet(key)
with open("target_file.txt","rb")as f:
	original_data=f.read()
encrypted_data=cipher.encrypt(original_data)
with open("target_file.txt","wb")as f:
	f.write(encrypted_data)
print(f"[+]File encryption successfully!")
print(f"[!]Keep this key to decrypt later:{key.decode()}")
