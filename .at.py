import os
import requests
import sys
import time


Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan

os.system ("python3 .k.py")

space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n        CYBER ATTACK ❤️❤️ \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n     ATTACKED BY ......\n\n\n️"

txt  = input("What Is Your Spam Text: ")

print ("")
print ("")
print ("")
print ("")

idadi  =  int(input("Enter Number Of Text Spam To Sent" + G+ "[No. Only]" +B+": "))

print ("")
print ("")
print ("")
print ("")

time.sleep (2)

nam  = input("What Is Your Nick Name To Display: ")


head = "\n\n\n\n\n\nTHIS GROUP HAS GOT VISITORS!! ☺️☺️"

os.system ("clear")
time.sleep (2)

text = txt.upper()
name = nam.upper()


spam = head + space + text + name 


time.sleep (1)
os.system ("python3 .k.py")

print ("")

id = input(Y+ "Enter Tellegram Group Id: ")
print ("")
print ("")
print ("")
msg3 =   spam   # 'User Name: ', ' Password :']
#for msg3 in msg3

y = 0

x = idadi

while y <= x:
   try:
     my_link = 'https://api.telegram.org/bot2042371872:AAGCHt_EI-xlINBQfKGQOa642ROQ3IsbMGc/sendMessage?chat_id=-'+id+'-&text=\n This is Attack but dont curse me😎😎😎!! \n\nWHERE AM IN?? Thats cool😂😂\n\n\nBut.........\n\n\n\n' +msg3
     requests.get(my_link)
     time.sleep(0.2)

     y += 1
     z = "Spam {} Text Successfull Sent!!!"
     print (z.format(y))
   except Exception:
     time.sleep (2)

print (B + "\n\n [ATTACK SUCCESSFULL COMPLETED]")






#bot.polling(none_stop=False, interval=0, timeout=20)

#https://api.telegram.org/bot2042371872:AAGCHt_EI-xlINBQfKGQOa642ROQ3IsbMGc/getUpdates
