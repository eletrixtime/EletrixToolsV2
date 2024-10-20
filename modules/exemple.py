# Template Module
# Author: EletrixTime
import threading
import requests
import time
import win32api
import mdapi
EXEMPLE = "-"

def mymodule():
    print("This is a custom module")
def cli(args=None):
    print(args) #getting args
    mymodule()
def register_mdapi():
    mdapi.register_module("exemple",cli,desc="Template Module")