import socket
print("---Professional Port Scanner v1.0---")
target=input("Enter target IP to scan(e.g.,127.0.0.1):")
ports=[22,80,443]
print(f"\n Starting scan on target:{target}")
print("-"*40)
for port in ports:
    try :
       s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.settimeout(1.0)
       s.connet((target,port))
       print(f"[+]Port[port]: OPEN")
       s.close()
    except:
       print(f"[-]Port[port]: CLOSE")
print("-"*40)
print("[*]Scan Complete Successfully.")
