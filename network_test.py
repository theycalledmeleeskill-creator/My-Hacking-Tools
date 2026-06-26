import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[*]connecting to Google port 80...")
s.connect(("google.com",80))
print("[+] Connection Successful! The Door is OPEN.")
s.close()
