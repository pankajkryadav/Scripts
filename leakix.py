# uncompyle6 version 3.9.0a1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0]
# Embedded file name: grabip.py
# Compiled at: 2020-12-15 03:39:46
import requests, json, os
from colorama import Fore
from multiprocessing.dummy import Pool
banner = '\n\x1b[36;1m\n$$$$$$\\            $$$$$$\\                     $$\\       $$\\                           \n\\_$$  _|          $$  __$$\\                    $$ |      $$ |                          \n  $$ |   $$$$$$\\  $$ /  \\__| $$$$$$\\  $$$$$$\\  $$$$$$$\\  $$$$$$$\\   $$$$$$\\   $$$$$$\\  \n  $$ |  $$  __$$\\ $$ |$$$$\\ $$  __$$\\ \\____$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ \n  $$ |  $$ /  $$ |$$ |\\_$$ |$$ |  \\__|$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \\__|\n  $$ |  $$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      \n$$$$$$\\ $$$$$$$  |\\$$$$$$  |$$ |     \\$$$$$$$ |$$$$$$$  |$$$$$$$  |\\$$$$$$$\\ $$ |      \n\\______|$$  ____/  \\______/ \\__|      \\_______|\\_______/ \\_______/  \\_______|\\__|      \n        $$ |                                                                           \n        $$ |                                                                           \n        \\__|                                                                          \n\t\n\t [ C0ded by #No_Identity ]\x1b[36;1m\n\t Ip Grabber For SMTP V2 Custom ApiKey\n\t https://t.me/xxyz4\n'
print banner
try:
    q = raw_input(Fore.LIGHTGREEN_EX + '\t root@youez:~# Query : ')
    thread = raw_input(Fore.RED + '\t root@youez:~# Thread : ')
    apikey = raw_input(Fore.LIGHTGREEN_EX + '\t root@youez:~# ApiKey : ')
    xx = int(thread)
    zx = Pool(xx)
    if q:
        pass
    else:
        q = '*'
    all_page = 500
    for t in range(all_page):
        print Fore.LIGHTGREEN_EX + 'Halaman :' + str(t)
        u = 'https://leakix.net/search?page=' + str(t) + '&q=' + q + '&scope=leak'
        headers = {'api-key': apikey, 
           'Accept': 'application/json'}
        x = requests.get(u, headers=headers)
        try:
            j = json.loads(x.text)
            for z in j:
                if ':' in z:
                    pass
                else:
                    print Fore.CYAN + z['ip']
                    fx = open('ips-result.txt', 'a')
                    fx.write(z['ip'] + '\n')
                    fx.close()

        except:
            print Fore.RED + 'Limit Page !'

except:
    print Fore.RED + 'Error' + Fore.WHITE
# okay decompiling grabip.pyc
