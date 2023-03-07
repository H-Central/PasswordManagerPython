import json

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
            site = input("What is your website or application ?\n")
            if list.get(site) != None:
                print("This website is already here.")
            else:
                passwd = input("What password do you want ?\n")
                list[site] = passwd
        case "3":
            see = input("What website or application you want to see the password\n")
            if list.get(see) == None:
                print("There are no password matching\n")
            else:
                print("Your password is:\n" + list.get(see))
        case "4":
            # here need to dev
            pass
        case "5":
            savePSW()
            print("See you later")
            break
        case other:
            savePSW()
            print("Not avable")
            continue
