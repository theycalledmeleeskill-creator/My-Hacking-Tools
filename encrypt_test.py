from cryptography.fernet import  Fernet
print("---Basic Malware Encryption Logic---")
key = Fernet.generate_key()
cipher=Fernet(key)
secret_message="This is a highly secret document!".encode()
encrypted_message=cipher.encrypt(secret_message)
print(f"[+]Original Key:[key.decode()]")
print(f"p[+]Encrypted Message :{encrypted_message.decode()}")
