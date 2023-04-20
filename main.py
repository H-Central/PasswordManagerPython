from helpers import manager, encode, gen
from time import sleep
import os

if os.path.exists(".key"):
    # encode.decrypt()
    print("Welcome to your password manager.")
    print()
else:
    print('you need to save the file ".key" in security')
    encode.genKEY()
    print("Welcome to your password manager.")
    print()

while True:
    print()
    print("What do you want to do")
    print("1 - Generate a password")
    print("2 - Add a password")
    print("3 - See a password")
    print("4 - Del a password")
    print("5 - Exit")

    choice = input()

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
            manager.delPSW()
            sleep(2)
        case "5":
            manager.savePSW()
            encode.crypter()
            print("See you later")
            sleep(2)
            break
        case other:
            manager.savePSW()
            print("Not avable")
            sleep(2)
            continue
