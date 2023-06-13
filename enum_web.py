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

    if not os.path.isfile(wordlist_dirsearch):
        print(colored("[!] Wordlist dirsearch not found!", 'red'))
        exit()
    if not os.path.isfile(wordlist_subdomain):
        print(colored("[!] Wordlist subdomain not found!", 'red'))
        exit()

    # Check if gobuster is installed
    if os.system("which gobuster") != 0:
        print(colored("[!] Gobuster not found!", 'red'))
        print(colored("[!] Please install gobuster : sudo apt-get install gobuster", 'red'))
        exit()
    # Check if nikto is installed
    if os.system("which nikto") != 0:
        print(colored("[!] Nikto not found!", 'red'))
        print(colored("[!] Please install nikto : sudo apt-get install nikto", 'red'))
        exit()
    # Check if nmap is installed
    if os.system("which nmap") != 0:
        print(colored("[!] Nmap not found!", 'red'))
        print(colored("[!] Please install nmap : sudo apt-get install nmap", 'red'))
        exit()

    # Check if gnome-terminal is installed
    if os.system("which gnome-terminal") != 0:
        print(colored("[!] gnome-terminal not found!", 'red'))
        print(colored("[!] Please install gnome-terminal : sudo apt-get install gnome-terminal", 'red'))
        exit()


def main():
    # url = input("Please enter the URL : ")
    url = "10.10.110.100"
    ip = socket.gethostbyname(url)
    port = "65000"
    if port != "":
        url = url + ":" + port

    path_dir = "reports/" + url
    create_dir(path_dir)

    wordlist_subdomain = "wordlist/subdomain/subdomains-top1mil-20000.txt"
    wordlist_dirsearch = "wordlist/directory/common.txt"
    check_requirements(wordlist_dirsearch, wordlist_subdomain)

    # print('The Port is :', port)
    print('The IP Address is :', ip)
    os.system('gnome-terminal -- bash -c "nikto +h ' + url + ' -output ' + path_dir + '/nikto.txt && bash"')
    os.system(
        'gnome-terminal -- bash -c " gobuster vhost -w ' + wordlist_subdomain + ' -u http://' + url + ' -t 50 --append-domain  -o ' + path_dir + '/subdomain.txt && bash"')
    os.system(
        'gnome-terminal -- bash -c " gobuster dir -u http://' + url + ' -w ' + wordlist_dirsearch + ' -t 50  -o ' + path_dir + '/dirsearch.txt && bash"')


if __name__ == '__main__':
    main()
