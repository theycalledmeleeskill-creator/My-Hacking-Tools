import socket
print("--Professional Port Scanner---")
target =input("Enter target IP to Scan (e.g.,127.0.0.10): ")
ports=[22,80,443]

print(f"\ည[*] Starting scan on target : {target}")
print("-"*40)
for port in ports:
     try:
         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         s.settimeout(2.0)
         s.connect((target,port))
         print(f"[+]Port {port}: OPEN!")
     except:
         print(f"[-] Port {port}]: CLOSED!")
print("_"*40)
print("[+] Scan complete successfully!")
