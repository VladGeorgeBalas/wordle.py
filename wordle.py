import random
from termcolor import colored

f = open("5word.txt", 'r')
words = [i for i in f.read().splitlines()]
curent = words[random.randrange(start=1, stop=len(words))]

count = 6
print("enter a word to begin, max 5 letters, must be a valid word\nYou have " + str(count) + " tries")

i = 1
while i < count:
    imp = input()
    if len(imp) != 5:
        print("lenght not valid")
        continue

    if not(imp in words):
        print("word is not valid")
        continue

    for j in range(0, 5):
        if imp[j] == curent[j]:
            print(colored(imp[j], 'green'), end='')
        else:
            if imp[j] in curent:
                print(colored(imp[j], 'yellow'), end='')
            else:
                print(colored(imp[j], 'red'), end='')
    print('')

    i+=1

print(colored(curent, 'cyan'))