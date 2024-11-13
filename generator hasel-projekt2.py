import random
print("Witaj w GENERATORZE HASEŁ")
print("Twoje hasło będzie zawierało 15 znaków , w tym litery , cyfry oraz znaki specjalne")

czesci_hasla = 'abcdefghijklmnoprstuwyxzABCDEFGHIJKLMNOPRSTUWYXZ.,<?>!£@#$%^&*()-_=+34567890'

input("Czy jesteś gotowy na otrzymanie twojego nowego hasla?  ")

haslo = ''

for i in range(15):
    haslo += random.choice(czesci_hasla)
print("Oto twoje haslo: ",haslo)


















