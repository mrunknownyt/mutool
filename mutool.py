import os
import sys
from core import *
from time import sleep as timeout 
from termcolor import colored

def menu():
 os.system("clear")
 print (colored("""
     .88b  d88. db    db d888888b  .d88b.   .d88b.  db      
     88'YbdP`88 88    88 `~~88~~' .8P  Y8. .8P  Y8. 88      
     88  88  88 88    88    88    88    88 88    88 88      
     88  88  88 88    88    88    88    88 88    88 88      
     88  88  88 88b  d88    88    `8b  d8' `8b  d8' 88booo. 
     YP  YP  YP ~Y8888P'    YP     `Y88P'   `Y88P'  Y88888P 

 >> CODED BY:AFEEF
 >> Youtube:   mr unknown
 >> Instagram: @afeef._.maf
 >> Telegram:  mrunknownyt 
 >>>TOOLS HAVE VIDEO TUTORIALS<<<
 ===============================================
 1. Fun Tools 
 2. Account Penatration
 3. Website Penetration
 4. Information Gathering
 5. Follow Me!               
 ================================================
 0. EXIT
 """,'red'))

loop = True

while loop:
    menu()
    mut =input("mutool > ")

    if mut == "1":
          os.system("clear")
          fun()
    elif mut == "2":
          os.system("clear")
          acp()
    elif mut == "3":
          os.system("clear")
          web()
    elif mut == "4":
          os.system("clear")
          ing()
    elif mut == "5":
          os.system("clear")
          folm()
    elif mut == "0":
        sys.exit()
    else:
                  print  (colored("ERROR: WRONG COMMAND BRO :(", 'red'))
                  timeout(1.5)
                  menu()
