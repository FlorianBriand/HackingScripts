#!/usr/bin/python3

import os
import socket

from art import *
from termcolor import colored


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


print(colored(text2art("SiteScan"), 'cyan'))


def check_requirements(wordlist_dirsearch, wordlist_subdomain):
    print(colored("[+] Checking Requirements...", 'green'))

    os.system("python3 -m pip install -r requirements.txt")

    required_tools = ["gobuster", "nikto", "nmap", "gnome-terminal"]
    for tool in required_tools:
        if os.system(f"which {tool}") != 0:
            print(colored(f"[!] {tool} not found!", 'red'))
            print(colored(f"[!] Please install {tool}: sudo apt-get install {tool}", 'red'))
            exit()

    if not os.path.isfile(wordlist_dirsearch):
        print(colored("[!] Wordlist dirsearch not found!", 'red'))
        exit()
    if not os.path.isfile(wordlist_subdomain):
        print(colored("[!] Wordlist subdomain not found!", 'red'))
        exit()



def main():
    # url = input("Please enter the URL : ")
    url = "10.10.110.100"
    # url = "172.16.1.19"

    ip = socket.gethostbyname(url)
    port = "65000"
    #port = "8080"
    if port != "":
        url = url + ":" + port

    path_dir = "reports/" + url
    create_dir(path_dir)

    wordlist_subdomain = "wordlist/subdomain/subdomains-top1mil-20000.txt"
    wordlist_dirsearch = "wordlist/directory/common.txt"
    check_requirements(wordlist_dirsearch, wordlist_subdomain)

    # print('The Port is :', port)
    print('The IP Address is :', ip)
    # nikto +h 10.10.110.100:65000

    command_nikto = "nikto +h " + url + " | tee " + path_dir + "/nikto.txt "
    print("Command Nikto : " + command_nikto)
    os.system('gnome-terminal -- bash -c "' + command_nikto + ' && bash"')

    # gobuster vhost -w wordlist/subdomain/subdomains-top1mil-20000.txt -u http://10.10.110.100:65000 -t 50 --append-domain
    command_gobuster_subdomain = "gobuster vhost -u http://" + url + " -w " + wordlist_subdomain + " -t 50 | tee " + path_dir + "/subdomain.txt "
    print("Command Gobuster Subdomain : " + command_gobuster_subdomain)
    os.system(
        'gnome-terminal -- bash -c "' + command_gobuster_subdomain + ' && bash"')

    # gobuster dir -u http://172.16.1.19:8080 -w wordlist/directory/common.txt -t 50

    command_gobuster_dir = "gobuster dir -u http://" + url + " -w " + wordlist_dirsearch + " -t 50  | tee " + path_dir + "/dirsearch.txt "
    print("Command Gobuster Dir : " + command_gobuster_dir)
    os.system(
        'gnome-terminal -- bash -c "' + command_gobuster_dir + ' && bash"')


if __name__ == '__main__':
    main()
