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

nmap_report = '''
Nmap scan report for 172.16.1.101
Host is up (0.00026s latency).
Bug in uptime-agent-info: no string output.
PORT      STATE SERVICE       VERSION
21/tcp    open  ftp           FileZilla ftpd
| ftp-syst:
|_  SYST: UNIX emulated by FileZilla
22/tcp    open  tcpwrapped
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp    open  http          Apache httpd 2.4.41
|_http-title: Index of /
25/tcp    open  tcpwrapped
70/tcp    open  tcpwrapped

Nmap scan report for 172.16.1.20
Host is up (0.83s latency).
Bug in http-title: no string output.
Bug in http-title: no string output.
Bug in uptime-agent-info: no string output.
PORT      STATE SERVICE            VERSION
22/tcp    open  ssh                OpenSSH for_Windows_8.1 (protocol 2.0)
25/tcp    open  tcpwrapped
80/tcp    open  http               Microsoft IIS httpd 8.5
|_http-server-header: Microsoft-IIS/8.5
'''

web_servers = extract_web_servers(nmap_report)
for server in web_servers:
    print("IP:", server[0], "Port:", server[1])
