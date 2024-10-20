
'''
Module API for registering custom modules
'''

from colorama import init, Fore, Back, Style
import os


MODULES_LIST = {} # {[{"name":"test","main_function":test"}]}
class logs():
    def register_error(text,module="Unknow",critical=False):
        if critical:
            print(Fore.RED + f"[ELETRIXTOOLS][MODULE-CRITICAL-ERROR] : {text}")
        else:
            print(Fore.RED + f"[ELETRIXTOOLS][MODULE-ERROR] : {text}")
    def register_info(text,module="Unknow"):
        print(Fore.GREEN + f"[ELETRIXTOOLS][MODULE-INFO] : {text}")
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def register_module(module_name,module_main_function,desc):
    MODULES_LIST[module_name] = {"name":module_name,"main_function":module_main_function,"desc":desc}
    return

def init():
    for i in os.listdir("modules"):
        if i.endswith(".py"):
            try:
                exec(f"from modules import {i[:-3]};{i[:-3]}.register_mdapi()")
                
            except Exception as e:
                pass