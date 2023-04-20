import json

def savePSW(liste):
    with open('data.json', 'w') as file:
        json.dump(liste, file)

def addPSW(liste):
    with open('data.json', 'r') as file:
        liste = json.load(file)
    site = input("What is your website or application ?\n")
    if liste.get(site) != None:
        print("This website is already here.")
    else:
        passwd = input("What password do you want ?\n")
        liste[site] = passwd
        savePSW()

def delPSW():
    pass

def seePSW(liste):
    see = input("What website or application you want to see the password\n")
    if liste.get(see) == None:
        print("There are no password matching\n")
    else:
        print("Your password is:\n" + list.get(see))