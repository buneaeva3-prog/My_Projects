# check_hosts_v2.py

# Input hosts file (you can rename this)
hosts_file = "hosts.txt"
# Output results file
output_file = "result.csv"


import time

# Read and clean hosts data
with open(hosts_file, "r") as file:
    hosts_data = []
    for line in file:
        line = line.strip()
        # Skip comments and blank lines
        if not line or line.startswith("#"):
            continue
        # Split to get only IP (before any hostname)
        parts = line.split()
        if parts:
            hosts_data.append(parts[0])

# Write results
with open(output_file, "w") as result:
    # Header
    result.write("IP,Hosts file?\n")

    # Nested loops for both IP ranges
    for i in range(10, 12):  # 10 and 11
        for j in range(1, 255):  # 1–254 inclusive
            ip = f"172.16.{i}.{j}"
            if ip in hosts_data:
                status = "Successful"
            else:
                status = "Failed"
            result.write(f"{ip},{status}\n")
            print(ip + " " + status)
            time.sleep(1)  
print('Inside of inneloop')
