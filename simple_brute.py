import string
from colorama import *
init()
running = True
pw = input("Let me crack your Password: \n")

def Brute(pw):
   print("[+][+][+] Starting BruteForce Crack attempt ...")
   charset = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
   result = ""
   x = 0
   while x <= len(pw) -1:
     for char in charset:
       pwchar = pw[x]
       if char == pwchar:
         print(Fore.GREEN +"[+] Cracking ..." + Style.RESET_ALL , char)
         print(Fore.LIGHTGREEN_EX + "[+][+]Matched (" + Style.RESET_ALL ,char, ")")
         result += char
         print("[+][+]Current:", result)
         x += 1
         break
       else:
         print(Fore.GREEN + "[+] Cracking ..." + Style.RESET_ALL,char)
   print(Fore.YELLOW + "[+][+][+] Done. Password cracking finished:", result + Style.RESET_ALL)
   finish = input("Press any key to end...")
   
Brute(pw)