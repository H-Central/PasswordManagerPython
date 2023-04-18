from helpers import manager, encode, gen
from time import sleep


print("Welcome to your password manager.")
print("It is your first time here ? (1 - no)(2 - yes)")
while True:
    choice = input(":")
    match choice:
        case "1" | "no":
            print("Your welcome")
            break
        case "2" | "yes":
            print("Okay we need to generate a key")
            print('For this you need to save the file "key.key" in security')
            encode.genKEY()
            break
        case other:
            print(f"You can't set \"{choice}\"")
            continue

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
            continue
