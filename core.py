import os
import sys
from time import sleep as timeout 
from termcolor import colored
##mainfuntion
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
    mut =int(input("mutool > "))

    if mut == 1:
          os.system("clear")
          fun()
    elif mut == 2:
          os.system("clear")
          acp()
    elif mut == 3:
          os.system("clear")
          web()
    elif mut == 4:
          os.system("clear")
          ing()
    elif mut == 5:
          os.system("clear")
          folm()
    elif mut == 0:
        sys.exit()
    else:
                  print  (colored("ERROR: WRONG COMMAND BRO :(", 'red'))
                  timeout(1)
                  menu()

##functions
def check():
 os.system("clear")
 print(colored("""      
        =================================================
        1. Installing tool
        2. video tutorial
        =================================================
        0. Back to main menu
        =================================================
 """, "blue"))
 global mutn
 mutn = int(input("mut > "))
 return mutn
###pranking
def fun():
  print(colored("""	
        =================================================
	1. Tbomb
	2. Pbomb
	3. Fake call (website)
	4. Instagram bot
	5. virtex (bomb)
	=================================================
	0. Back to main menu
	=================================================
  """, "blue"))

  mut = int(input("mut > "))
  if mut==1:
        check()
        if mutn==1:
		os.system("installation started | lolcat -a && git clone https://github.com/TheSpeedX/TBomb.git")
		os.system("mv TBomb ~")
		menu()
        elif mutn==2:
		os.system("termux-open-url https://youtu.be/U8RS6uPOoIU")
                menu()
	elif mutn==0:
                menu()
	else:
		print("ERROR:WRONG INPUT BRO...")
		fun()
  elif mut==2:
	check()
        if mutn==1:
		os.system("installation started | git clone https://github.com/HACK3RY2J/PBomb.git") 
                os.system("mv PBomb ~")
                menu()
        elif mutn==2:
                os.system("termux-open-url https://youtu.be/U8RS6uPOoIU")
                menu()
        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
		fun()
  elif mut==3:
        os.system("termux-open-url https://youtu.be/EUZ8sev1ouw")
        menu()

  elif mut==4:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/officialputuid/toolsig.git")
                os.system("mv toolsig ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/zYBmFGITLOk")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
		fun()
  elif mut==5:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/muhammadfathul/VIRTEX.git")
                os.system("mv VIRTEX ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/b333djLSbN8")
                menu()

        elif mutn==0: 
                menu()

        else:
                print("WRONG INPUT BRO...")
                fun()

  elif mut==0:
	menu()
  else:
	print("ERROR:WRONG INPUT BRO ")
	fun()
##accountpentesting
def acp():
  print(colored("""      
        =================================================
        1. shellphish
        2. zphisher
        3. multibf
        4. fotosploit
        5. advance phish
	6. seeker
	7. john the ripper
	8. saychees (front cam)
	9. sayhello 
        =================================================
        0. Back to main menu
        =================================================
  """, "blue"))

  mut = int(input("mut > "))

  if mut==1:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/thelinuxchoice/shellphish.git")
                os.system("mv shellphish ~")
                menu()
        elif mutn==2:
                os.system("termux-open-url https://youtu.be/3-ynS8LCA5A")
                menu()
        elif mutn==0:
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==2:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/htr-tech/zphisher.git")
                os.system("mv zphisher ~")
                menu()
        elif mutn==2:
                os.system("termux-open-url https://youtu.be/3xlBW7k6UiI")
                menu()
        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==3:
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/noolep/multiBF_ig.git")
                os.system("mv multiBF_ig ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/4fUeE81VsCY")
                menu()

        elif mutn==0: 
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()


  elif mut==4:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone clone https://github.com/Cesar-Hack-Gray/FotoSploit")
                os.system("mv FotoSploit ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/8V8ZEqOVf3o")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==5: 
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/Ignitetch/AdvPhishing.git")
                os.system("mv AdvPhishing ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/BSTQQ5kWyZ0")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==6: 
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/thewhiteh4t/seeker.git")
                os.system("mv seeker ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/mNUwsmohUNU")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==7: 
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/magnumripper/JohnTheRipper.git")
                os.system("mv JohnTheRipper ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/PvuwhENaq0w")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==8: 
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/thelinuxchoice/saycheese.git")
                os.system("mv saycheese ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/OVbf-kthXJA")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()
  elif mut==9: 
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/greyli/sayhello.git")
                os.system("mv sayhello ~")
                menu()

        elif mutn==2:
                os.system("termux-open-url https://youtu.be/x94XU94sIwk")
                menu()

        elif mutn==0:
                menu()

        else:
                print("WRONG INPUT BRO...")
                acp()

  elif mut==0: 
        menu()

  else:
	print("ERROR:WRONG INPUT BRO.")
        acp()

###webpentesting
def web():
  print(colored("""      
        =================================================
        1. websloit
        2. routersplot
        3. sqlmap
        4. metasploit 
        =================================================
        0. Back to main menu
        =================================================
  """, "blue"))

  mut = int(input("mut > "))

  if mut==1:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/websploit/websploit.git")
                os.system("mv websploit ~")
                menu()
        elif mutn==2:
                os.system("termux-open-url https://youtu.be/zNzr7korilQ")
                menu()
        elif mutn==0:
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==2:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/threat9/routersploit.git")
                os.system("mv routersploit~")
                menu()
        elif mutn==2: 
                os.system("termux-open-url https://youtu.be/zEBcyC3gJmo")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==3:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/sqlmapproject/sqlmap.git")
                os.system("mv sqlmap ~")
                menu()
        elif mutn==2: 
                os.system("termux-open-url ")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()


  elif mut==4:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && pkg install unstable-repo")
                os.system("pkg install metasploit")
                menu()
        elif mutn==2: 
                os.system("termux-open-url https://youtu.be/MzbDtcH_maE")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()

  elif mut=="0": 
        menu()

  else:
        print("ERROR:WRONG INPUT BRO.")
        acp()

###informationgathering

def web():
  print(colored("""      
        =================================================
        1. phoneinfoga (data of mobile no)
        2. sherlock
        3. user recon
        4. redhawk (website)
	5. metapicz (from a image)
        =================================================
        0. Back to main menu
        =================================================
  """, "blue"))

  mut = int(input("mut > "))

  if mut==1:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/abhinavkavuri/PhoneInfoga.git")
                os.system("mv PhoneInfoga ~")
                menu()
        elif mutn==2:
                os.system("termux-open-url https://youtu.be/HFdu_gB-jI4")
                menu()
        elif mutn==0:
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==2:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/sherlock-project/sherlock.git")
                os.system("mv sherlock ~")
                menu()
        elif mutn==2: 
                os.system("termux-open-url https://youtu.be/PEIxnLKxtRA")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==3:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/thelinuxchoice/userrecon.git")
                os.system("mv userrecon ~")
                menu()
        elif mutn==2: 
                os.system("termux-open-url https://youtu.be/cNl0IXuFK4Y")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==4:
        check()
        if mutn==1:
                os.system("installation started | lolcat -a && git clone https://github.com/RedhawkSDR/redhawk.git")
                os.system("mv redhawk ~")
                menu()
        elif mutn==2: 
                os.system("termux-open-url https://youtu.be/XRs6rWx2ipk")
                menu()
        elif mutn==0: 
                menu()
        else:
                print("ERROR:WRONG INPUT BRO...")
                acp()
  elif mut==5:
        os.system("termux-open-url https://youtu.be/0wiQ2hLfR1o")

  elif mut==0: 
        menu()

  else:
        print("ERROR:WRONG INPUT BRO.")
        acp()

###followas

def follow():
 print(colored("""
  #######################
  1. Follow Blogger
  2. Follow telegram 
  3. Follow Instagram
  4. Follow YouTube Channel
  ########################
  """, "green"))
 visit = input("go > ")
 if visit == "1":
  os.system("termux-open-url https://mrunknown-yt.blogspot.com/")
 elif visit == "2":
  os.system("termux-open-url https://t.me/mrunknownyt")
 elif visit == "3":
  os.system("termux-open-url https://www.instagram.com/afeef._.maf/")
 elif visit == "4":
  os.system("termux-open-url https://www.youtube.com/channel/UCtVzQz_FEQTaU3fXeEYqetQ/")
 else:
  print("ERROR:WRONG INPUT BRO :(")
