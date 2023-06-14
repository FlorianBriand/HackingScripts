import requests

TIMEOUT = 1


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
        if "/tcp" and "open" in line:
            # split the line to get the port
            port = line.split()[0].split("/")[0]
            ip_ports.append((ip, port))
    return ip_ports


def get_webpage(ip, port):
    url = f"http://{ip}:{port}"

    try:
        # Send a request to the URL if no response is received within 10 seconds, an exception will be raised
        response = requests.get(url, verify=False, timeout=TIMEOUT)
        print(f"Found {url} with status code {response.status_code}")
        return (ip, port)

        # If an exception is raised
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {str(e)}")
        return None


def extract_ip_and_ports_webpage(report):

    ip_ports = extract_ip_and_ports(report)

    print(ip_ports)

    list_webpage = []

    for ip, port in ip_ports:
        print(f"Checking {ip}:{port}")
        webpage = get_webpage(ip, port)
        if webpage:
            list_webpage.append(webpage)

    print(list_webpage)

    return list_webpage
