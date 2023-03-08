from random import choice, randint

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
higer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

def pwd(n , low = True, hig = True, num = True, spe = True):
    alphabets = dict()
    key = 0
    if low:
        alphabets[key] = lower
        key += 1
    if hig:
        alphabets[key] = higer
        key += 1
    if num:
        alphabets[key] = number
        key += 1
    if spe:
        alphabets[key] = special
        key += 1

    mdp = ''
    for i in range(n):
            s = randint(0,key-1)
            mdp += choice( alphabets[s] )
            
    print("And your password is:\n" + mdp)


def genPSD():
    print("What do you want for the longuest of the password:")
    long = input()
    long = int(long)
    pwd(long)