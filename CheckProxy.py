#!/usr/bin/python3
import os,  time, requests, sys, threading
CheckVersion = str(sys.version)

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()




def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = sess.get(url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 200:
            print (PROXY + '   GooD')
            with open('OKproxy.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print (PROXY + '   BaD')
    except:
        print (PROXY + '   BaD')


def main():
    try:
        if '3.' in CheckVersion:
            try:
                fileproxy = input(' Proxy.txt --> ')
            except:
                print('  [-] Error : Enter Your Proxy!')
                sys.exit()
        elif '2.' in CheckVersion:
            try:
                fileproxy = raw_input(' Proxy.txt --> ')
            except:
                print('  [-] Error : Enter Your Proxy!')
                sys.exit()
        else:
            print(' Unknown Python Version!')
    except:
        pass
        sys.exit()
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://instagram.com'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for j in thread:
        j.join()

main()



