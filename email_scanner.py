import re

print("--- Automated Email Harvester (Local Test) ---")

# ၁။ စောစောက ဆောက်လိုက်တဲ့ mock_web.txt ဖိုင်ကို လှမ်းဖတ်ခြင်း
with open("mock_web.txt", "r") as f:
    web_text = f.read()

# ၂။ အီးမေးလ်ပုံစံ (Regex Pattern)
email_pattern = r"[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

# ၃။ စာသားထဲက အီးမေးလ်တွေကို လိုက်ရှာခြင်း
found_emails = re.findall(email_pattern, web_text)

if found_emails:
    print(f"\n[+] SUCCESS: Found {len(found_emails)} emails!")
    print("-" * 40)
    for email in found_emails:
        print(f"[!] Email: {email}")
else:
    print("\n[-] No emails found.")

