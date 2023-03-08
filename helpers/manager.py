import json

def savePSW():
    with open('data.json', 'w') as file:
        json.dump(list, file)

def addPSW():
    site = input("What is your website or application ?\n")
    if list.get(site) != None:
        print("This website is already here.")
    else:
        passwd = input("What password do you want ?\n")
        list[site] = passwd

def seePSW():
    see = input("What website or application you want to see the password\n")
    if list.get(see) == None:
        print("There are no password matching\n")
    else:
        print("Your password is:\n" + list.get(see))

def selPSW():
    pass