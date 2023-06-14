import re


def extract_web_servers(report):
    web_servers = []
    lines = report.split('\n')
    for line in lines:
        match = re.search(r'Nmap scan report for (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        if match:
            ip = match.group(1)
        elif "http" in line:
            match = re.search(r'\b(\d+)/tcp\s+open\s+(\w+)', line)
            if match:
                port = match.group(1)
                service = match.group(2)
                if service == "http":
                    web_servers.append((ip, port))
    return web_servers


nmap_report = open("nmap.txt", "r").read()

web_servers = extract_web_servers(nmap_report)
for server in web_servers:
    print("IP:", server[0], "Port:", server[1])
