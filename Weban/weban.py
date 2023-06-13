#!/usr/bin/python3

import os
import socket
import sys

sys.path.append('__init__')
from art import *
from termcolor import colored


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


print(colored(text2art("Weban"), 'cyan'))


def main():
    # url = input("Please enter the URL : ")
    url = "danteweb1.htb"
    ip = socket.gethostbyname(url)
    port = "65000"
    if port != "":
        url = url + ":" + port

    path_dir = "reports/" + url
    create_dir(path_dir)

    # print('The Port is :', port)
    print('The IP Address is :', ip)
    os.system('gnome-terminal -- bash -c "nmap ' + ip + ' -o ' + path_dir + '/nmap.txt && bash"')
    os.system('gnome-terminal -- bash -c "nikto +h ' + url + ' -output ' + path_dir + '/nikto.txt && bash"')
    os.system(
        'gnome-terminal -- bash -c "python3 __init__/dirsearch/dirsearch.py -u ' + url + ' -e ' + path_dir + '/dirsearch.txt && bash"')


if __name__ == '__main__':
    main()
