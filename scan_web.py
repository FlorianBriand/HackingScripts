import os

from nmap import extract_ip_and_ports_webpage


def save_list_web_server(list_web_server):
    # check dir exist
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    # save list_web_server
    file = open("tmp/list_web_server.txt", 'w')
    file.write(str(list_web_server))
    file.close()


report = open("nmap.txt", "r").read()

save_list_web_server(extract_ip_and_ports_webpage(report))

def get_list_web_server():
    # check dir exist
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    #Check if file exist
    if not os.path.exists("tmp/list_web_server.txt"):
        print("File tmp/list_web_server.txt not found")
        save_list_web_server(extract_ip_and_ports_webpage(report))
    file = open("tmp/list_web_server.txt", 'r')
    list_web_server = eval(file.read())
    file.close()
    return list_web_server


liste_web_server = get_list_web_server()

for ip, port in liste_web_server:
    command = "python3 enum_web.py -u " + ip + " -p " + port
    os.system(command)

    # Progress
    print("Progress: " + str(liste_web_server.index((ip, port)) + 1) + "/" + str(len(liste_web_server)))
    # Wait for the user to press enter
    input("Press Enter to continue...")