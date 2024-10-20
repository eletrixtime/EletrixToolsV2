'''
Main file :/
'''

from colorama import init, Fore, Back, Style
import threading
import requests
import time
import win32api
import os
# modules
from modules import ddos,chat
import mdapi
mdapi.init()
if mdapi.MODULES_LIST != {}:
    for i in mdapi.MODULES_LIST:
        print(Fore.GREEN + f"Registered module : {i}")
        exec(f"from modules import {i}")

#====

win32api.SetConsoleTitle("EletrixTools")
name = win32api.GetComputerName()
_VERSION = "0.0.1"
print(Fore.GREEN + f"""
 _____ _      _        _    _____           _     
|  ___| |    | |      (_)  |_   _|         | |    
| |__ | | ___| |_ _ __ ___  _| | ___   ___ | |___ 
|  __|| |/ _ \ __| '__| \ \/ / |/ _ \ / _ \| / __|
| |___| |  __/ |_| |  | |>  <| | (_) | (_) | \__ \
      
\____/|_|\___|\__|_|  |_/_/\_\_/\___/ \___/|_|___/
                            
>  VERSION {_VERSION}
> Use this software at your own risk!

""")
print("Made by EletrixTime ^^")
while True:
    x = input(Fore.GREEN + f"EletrixTools@{name}" + Fore.RED + " > " + Fore.WHITE)
    x = x.split(" ")
    if x[0] == "exit":
        print(Fore.GREEN + "Goodbye!")
        break
    elif x[0] == "help":
        print(Fore.GREEN + "Available commands:")
        print(Fore.GREEN + "help" + Fore.WHITE + " - Show this help")
        print(Fore.GREEN + "ddos" + Fore.WHITE + " - Attack a target")
        print(Fore.GREEN + "chat" + Fore.WHITE + " - Just talk...")
        print(Fore.GREEN + "clear" + Fore.WHITE + " - Clear the screen")
        print(Fore.GREEN + "exit" + Fore.WHITE + " - Exit EletrixTools")
        print("=================")
        print("CUSTOM MODULES")
        for i in mdapi.MODULES_LIST:
            print(Fore.GREEN + f"{i}" + Fore.WHITE + f" - {mdapi.MODULES_LIST[i]['desc']}")
    elif x[0] == "clear":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    elif x[0] == "chat":
        chat.cli(args=x)
    elif x[0] == "ddos":
        ddos.cli(args=x)
    else:
        if x[0] in mdapi.MODULES_LIST:
            print("LAUNCHING CUSTOM MODULE")
            mdapi.MODULES_LIST[x[0]]["main_function"](args=x)
        else:
            print(Fore.RED + "Command not found!")