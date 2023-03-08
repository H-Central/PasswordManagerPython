import json
from DeltacodeProject.encodings2 import *
from DeltacodeProject.Deltacode import Deltacode as menu
# pip install DeltacodeProject
from helpers import manager, encode, gen
from time import sleep
from os import system as cmd
from os import name as osname

default_password = "@pà$$£0rµ"

with open('data.json', 'r') as file:
    list = json.load(file)

while True:
    cmd("clear" if osname == "posix" else "cls")
    choice = input("What do you want to do\n" + menu().create_menu(2, [
        "Generate a password",
        "Add a password",
        "See a password",
        "Del a password",
        '',
        "Exit"
    ]))
    match choice:
        case "1":
            gen.genPSD()
            sleep(2)
        case "2":
            manager.addPSW()
            sleep(2)
        case "3":
            manager.seePSW()
            sleep(2)
        case "4":
            manager.delPSD()
        case "5":
            manager.savePSW()
            print("See you later")
            sleep(2)
            break
        case other:
            manager.savePSW()
            print("Not avable")
            sleep(2)
