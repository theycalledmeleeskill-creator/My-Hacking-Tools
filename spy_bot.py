import re
from cryptography.fernet import Fernet
print("---Automated Scan Hamvester v1.0---")
print("[*] Task1 :Scraping emails from source...")
with open("mock_web.txt","r")as f:
        web_text=f.read()
email_pattern = r"[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
found_emails=re.findall(email_pattern,web_text)
print("[*]Task 2: Saving stolen data info file...")
with open("stolen_emails.txt","w")as f:
        f.write("---Stolen Email database---\n")
        for email in found_emails:
                f.write(f"[!]{email}\n")
print("[*] Task 3: Encrypting the evidence file...")

# သော့ချက် (Key) ဆောက်ခြင်း
key = Fernet.generate_key()
cipher = Fernet(key)

# stolen_emails.txt ကို Read Binary ("rb") ဖြင့် ပြန်ဖတ်ခြင်း
with open("stolen_emails.txt", "rb") as f:
    original_data = f.read()

# ဒေတာကို သော့ခတ် (Encrypt) ခြင်း
encrypted_data = cipher.encrypt(original_data)

# သော့ခတ်ပြီးသားဒေတာကို Write Binary ("wb") ဖြင့် ဇွတ်ပြန်သိမ်းခြင်း
with open("stolen_emails.txt", "wb") as f:
    f.write(encrypted_data)

print("-" * 50)
print("[+] SUCCESS: Spy Bot mission completed!")
print(f"[!] Decryption Key: {key.decode()}")
print("-" * 50)
