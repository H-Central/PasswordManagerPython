import json

def savePSW(a):
    with open('data.json', 'w') as file:
        json.dump(a, file)

def addPSW():
    with open('data.json', 'r') as file:
        pswl = json.load(file)
    site = input("What is your website or application ?\n")
    if pswl.get(site) != None:
        print("This website is already here.")
    else:
        passwd = input("What password do you want ?\n")
        pswl[site] = passwd
        savePSW(a = pswl)

def delPSW():
    pass

def seePSW():
    savePSW()
    with open('data.json', 'r') as file:
        pswl = json.load(file)
    see = input("What website or application you want to see the password\n")
    if pswl.get(see) == None:
        print("There are no password matching\n")
    else:
        print("Your password is:\n" + pswl.get(see))