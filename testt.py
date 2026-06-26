import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2.0)
print("[*]Testing Port 999 on Google.com(This port is usually closed)")
try:
	s.connect(("google.com",999))
	print("[*]Port 999 is OPEN!")
except:
	print("[*]Port 999 is CLOSED!'")
print("[*]Scripts finished without crashing")
