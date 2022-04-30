import os
import time
import pyfiglet
import phonenumbers 
from colorama import Fore 
from datetime import datetime   
from phonenumbers import geocoder 
from phonenumbers import carrier
from phonenumbers import timezone

#def. variables
l = "------------------"
t = time.sleep

result = pyfiglet.figlet_format("PhoneDNS")
print(result)

print(l)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}PhoneDNS {Fore.WHITE}Codex-ops{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
t(0.3)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Original creator: {Fore.WHITE}https://github.com/Codex-ops")
t(0.3)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Creator of this version : {Fore.WHITE}https://github.com/Codex-ops")
t(0.3)
t(2)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
t(2)

number = input("Enter number: ")
t(1)

#See if the numbers valid 
ch_nmber = phonenumbers.parse(number)
print(phonenumbers.is_possible_number(ch_nmber))
print(l)
t(0.5)

#Find their state
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))
print(l)
t(0.5)

#Find their carrier (Still in Development)
ch_nmber = phonenumbers.parse(number, "CH")
print(carrier.name_for_number(ch_nmber, "en"))
print(l)
t(0.5)

#Find their time zone 
ch_nmber = phonenumbers.parse(number)
print(timezone.time_zones_for_number(ch_nmber))
print(l)
t(0.5)
result = pyfiglet.figlet_format("PhoneDNS")
print(result)
print(l)

if os.name == "nt":
    os.system('cls')
elif os.name == "posix":
    os.system('clear')
t(3)

os.system('python osint.py')

if os.name == "nt":
    os.system('cls')
elif os.name == "posix":
    os.system('clear')
t(3)

os.system('python Osint2.py')

if os.name == "nt":
    os.system('cls')
elif os.name == "posix":
    os.system('clear')
t(3)

service_nmber = phonenumbers.parse(number, "CH")