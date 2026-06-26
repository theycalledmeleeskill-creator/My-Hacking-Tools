import subprocess
print("[*]Excuting System command via Python...")
result=subprocess.run(["ls","ls -a"],capture_output=True,text=True
print(f"[+]System Output: {result.stdout}")
