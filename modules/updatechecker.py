# Template Module
# Author: EletrixTime
# NOT COMPATIBLE WITH MDAPI

import threading
import requests
import time
import win32api
import mdapi
EXEMPLE = "-"

def mymodule():
    print("Todo")
def cli(args=None):
    print(args)
    mymodule()
def register_mdapi():
    mdapi.register_module("updatechecker",cli,desc="check for update")