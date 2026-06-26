import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[*]Connecting to Google Port 80...")
s.connect(("google.com",80))
print("[*]Connection Successful! The door is open")
s.close()
