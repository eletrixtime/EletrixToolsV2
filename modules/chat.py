# Template Module
# Author: EletrixTime
import threading
import requests
import time
import win32api
from colorama import init, Fore, Back, Style
import socket
import mdapi
# NOT COMPATIBLE WITH MDAPI


EXEMPLE = "Arguments missing use this example : chat [USERNAME]"



def mymodule(chat_url_="chat.eletrix.fr", chat_port_=80,username=""):
    skc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skc.connect((chat_url_, chat_port_))
    def receive_messages():
            while True:
                try:
                    message = skc.recv(1024).decode('utf-8')
                    if message:
                        print(Fore.YELLOW + f"\n{message}" + Style.RESET_ALL)
                    else:
                        mdapi.logs.register_error("Connection closed by server")
                        skc.close()
                        break
                except Exception as e:
                
                    break
    x = threading.Thread(target=receive_messages)
    x.start()
    inpd = None
    while inpd != "exit":
        inpd = input(Fore.GREEN + f"EletrixChat@{username}" + Fore.RED + " > " + Fore.WHITE)
        # send to the server
        fish = f"{username} : {inpd}"
        print(fish)
        skc.send(fish.encode("utf-8"))
    x.join()
    skc.close()
    return
def cli(args=None):
    print("EletrixChat - V0.0.1")
    print("THIS IS IN BETA")
    try:
        username = args[1] 
        # check if > 3 chars
        if len(username) < 3:
            print("Username too short!")
            return
        else:
            try:
                mymodule(username=username)
            except Exception as e:
                mdapi.logs.register_error(e,module="chat",critical=True)
                return
    except:
        print(EXEMPLE)
        return
