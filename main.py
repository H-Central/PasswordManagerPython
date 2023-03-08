import json
from helpers import manager, encode, gen

def savePSW():
    with open('data.json', 'w') as file:
        json.dump(list, file)

with open('data.json', 'r') as file:
    list = json.load(file)

while True:
    print("What do you want to do")
    print("1 - Generate a password")
    print("2 - Add a password")
    print("3 - See a password")
    print("4 - Del a password")
    print("5 - Exit")

    choice = input()

    match choice:
        case "1":
            # here need to dev
            pass
        case "2":
            manager.addPSW()
        case "3":
            manager.seePSW()
        case "4":
            manager.delPSD()
        case "5":
            savePSW()
            print("See you later")
            break
        case other:
            savePSW()
            print("Not avable")
            continue
