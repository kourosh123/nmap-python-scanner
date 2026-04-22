import subprocess

target = input("Enter target: ")

print(f"[+] Scanning {target} ...")

result = subprocess.run(
    ["nmap", "-sT", "-Pn", target],
    capture_output=True,
    text=True
)

output = result.stdout

print(output)

# Save output to file
filename = "scan_result.txt"

with open(filename, "w") as f:
    f.write(output)

print(f"\n[+] Report saved as {filename}")
