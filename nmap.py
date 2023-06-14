def extract_ip_and_ports(report):
    lines = report.strip().split('\n')
    ip_ports = []
    ip = ""
    for line in lines:
        # if the line match with "Nmap scan report for X.X.X.X"
        if "Nmap scan report for" in line:
            # split the line to get the IP
            ip = line.split()[4]
        # if the line match with x/tcp open
        if "/tcp" in line:
            # split the line to get the port
            port = line.split()[0].split("/")[0]
            ip_ports.append((ip, port))
    return ip_ports

def main():
    report = open("nmap.txt", "r").read()

    ip_ports = extract_ip_and_ports(report)

    print(ip_ports)


if __name__ == "__main__":
    main()
