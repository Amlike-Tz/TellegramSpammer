import time
import os
import sys

#Colours choosen by amlike
#Colours choosen by amlike


YELLOWBG = '\033[103m'
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'



show = "FIRST YOU HAVE TO GO TELLEGRAM AND SEAERCH THIS BOT 👉👉    \n\n  "+yellow+" @AttackerrBot     \n\n\n"+green+" Then Add that bot to a telegram group you wanner spamm Then come To this Tool Slect option 2 To get the id of That Group \n\n\n\n\n"+cy+"  After Select Option To you will see many Group Ids So Find The Name Of Group You Have Add The Bot inside \n\n\n\n\n Then check whrere Have wtiten Chat Id Copy That number"+yellow+" \n\n\n eg 4183883972  \n\n\nn"+B+"\n\n\n\n" +B+"Then.. Come To spammer Sellect Option 1 WHere You will See A place To paste That Id Then boom!! Your are Done."

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
 

os.system ("clear")
time.sleep (2)

os.system ("python .k.py")
print ("")
print (R+"       ➡ "+cyan+"[01] Tellegram Spam")
print ("")
print (R+"       ➡ "+cyan+"[02] Find 1st Your Spam Group ID")
print ("")
print (R+"       ➡ "+cyan+"[03] Check For Updates")
print ("")
print (R+"       ➡ "+cyan+"[04] Join Our Group")
print ("")
print (R+"       ➡ "+cyan+"[06] How To Use Spammer")
print ("")
print (R+"       ➡ "+cyan+"[x] Exit Script")
print ("")
time.sleep(1)
for i in range (10):
       com=input(R+"Enter your choice: ")
       if com=="01":
                os.system("clear")
                time.sleep(2)
                os.system("python .k.py")
                print ("")
                print ("")
                print (R+"       ➡ "+cyan+"[01] Single Attack")
                print ("")
                print (R+"       ➡ "+cyan+"[02] Unlimited Attack")
                print ("")
                print (R+"       ➡ "+cyan+"[03] Exit")
                print ("")
                for i in range (5):
                    com=input(R+"SELECT: ")
                    if com=="01":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .at.py")
                            sys.exit(1)
                            print ("")
                    elif com=="02":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .unl.py")
                            sys.exit(1)
                            print ("")    
                    elif com=="03":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                    else:
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
         

       elif com=="02":
                os.system("clear")
                time.sleep(2)
                os.system("figlet IDs")
                print ("")
                print ("")
                print (cyan+"Please wait Now is Tool is Requesting For Group Id" +R+" Make Sure You Have Already Add The AttackerrBot To a specific telegram Group"+cyan+"Then you may Continue with This")
                print ("")
                time.sleep(4)
                print ("")
                os.system ("bash .r.sh")
                sys.exit(1)
                print ("")
               
       elif com=="03":
                os.system("clear")
                os.system("clear")
                time.sleep(3)
                os.system("figlet Updates")
                time.sleep(2)
                print ("")
                print (yellow+"Tellegram Spammer Is Checking For Any Updates first---")
                time.sleep(2)
                os.system ("cd && rm -rf TellegramSpammer && git clone https://github.com/Amlike-Tz/TellegramSpammer.git  && cd TellegramSpammer && python3 start.py")
       elif com=="04":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  GOING TO JOIN US " + cyan+"DONT  Exit in your Termux DUDE")
                print ("")
                time.sleep(3)
                print ("")
                os.system("bash .asap.sh")
                sys.exit(1)
                print ("")

       elif com=="05":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
       elif com=="06":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  Pleas Wait Is Loading info...." + cyan+"DONT  Exit in your Termux DUDE")
                print ("")
                time.sleep(3)
                print ("")
                delay_print (show)
                os.system ("python3 start.py")
                

       elif com=="x":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  GOING TO EXIT " + cyan+"BYEEEE  AM  Exit in your Termux DUDE")
                print ("")
                time.sleep(3)
                print ("")
                sys.exit(1)
                print ("")
       else:
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  WRONG CHOOSEN " + cyan+ "TOOL IS BACK TO MAIN MENU  DUDE")
                print ("")
                time.sleep(3)
                print ("")
                os.system ("python3 start.py")
