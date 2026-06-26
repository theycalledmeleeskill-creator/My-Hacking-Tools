import subprocess

print("[*] Excuting system command via python")
result=subprocess.run(["ip","addr"],capture_output=True,text=True)
print(f"System output:{result.stdout}")
print("-"*50)
print(result.stdout)
print("-"*50)
