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
   
