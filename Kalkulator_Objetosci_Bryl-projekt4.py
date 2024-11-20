
print("Witaj w programie obliczajacym obejtosci bryl")

def szescian():
    a = int(input("Podaj dlugosc krawedzi: "))
    if a>0:
        return a**3
    else:
        return("Krawedzie nie moga byc ujemne lub rowne 0")

def prostopadloscian():
    a = int(input("Podaj dlugosc 1 krawedzi: "))
    b = int(input("Podaj dlugosc 2 krawedzi: "))
    c = int(input("Podaj dlugosc 3 krawedzi: "))
    if a>0 and b>0 and c>0:
        return a*b*c
    else:
        return("Zadna z krawedzi nie moze byc mniejsza lub rowna 0")

def graniastoslup():#trojkat w podstawie
    a = int(input("Podaj dlugosc 1 krawedzi podstawy: "))
    h = int(input("Podaj wysokosc podstawy: "))
    Pp = a*h/2
    H = int(input("Podaj wysokosc graniastoslupa: ")) 
    if Pp>0 and H>0:
        return Pp*H
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")

def graniastoslup2():#trapez w podstawie
    a = int(input("Podaj dlugosc 1 podstawy podstawy graniastoslupa: "))
    b = int(input("Podaj dlugosc 2 podsatawy podstawy graniastoslupa: "))
    h = int(input("Podaj wysokosc podstawy: "))
    Pp = (a+b)*h/2
    H = int(input("Podaj wysokosc graniastoslupa"))
    if Pp>0 and H>0:
        return Pp*H
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")

def ostroslup():#prostokat w podstawie
    a = int(input("Podaj dlugosc 1 krawedzi podstawy: "))
    b = int(input("Podaj dlugosc 2 krawedzi podstawy: "))
    Pp = a*b
    H = int(input("Podaj wysokosc graniastoslupa"))
    if Pp>0 and H>0:
        return Pp*H/3
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")

def ostroslup2():#trojkat w podstawie
    a = int(input("Podaj dlugosc krawedzi podstawy: "))
    h = int(input("Podaj wysokosc podstawy: "))
    Pp = a*h/2
    H = int(input("Podaj wysokosc graniastoslupa"))
    if Pp>0 and H>0:
        return Pp*H/3
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")

def kula():
   pi = 3,14
   r = int(input("Podaj promien kuli :")) 
   if r>0:
        return 4/3*pi*r**3
   else:
       return("Promien nie moze byc ujemny")
   
def stozek():
    pi = 3,14
    r = int(input("Wprowadz promien podstawy: "))
    H = int(input("Wprowadz wysokosc stozka: ")) 
    if r>0 and H>0:
        return pi*r**2*H/3
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")

def walec():
    pi = 3,14
    r = int(input("Podaj promien podstawy: "))
    H = int(input("Podaj wysokosc walca: "))
    if r>0 and H>0:
        return pi*r**2*H
    else:
        return("Zadna z dlugosci nie moze byc mniejsza lub rowna 0")
    

print("1. Objetosc Szescianu")
print("2. Objetosc prostopadloscianu")
print("3. Objetosc graniastoslupa o podstawie trojkata")
print("4. Objetosc graniastoslupa o podstawie trapezu")
print("5. Objetosc ostroslupa o podstawie prostokata")
print("6. Objetosc ostroslupa o podstawie trojkata")
print("7. Objetosc kuli")
print("8. Objetosc stozka")
print("9. Objetosc walca")

wybor = input("Wybierz opcję (1-9): ")
 
if wybor == "1":
    print(f"Objetosc Szescianu: {Objetosc_Szescianu():.2f}")
elif wybor == "2":
    print(f"Objetosc prostopadloscianu: {Objetosc_prostpadloscianiu():.2f}")
elif wybor == "3":
    print(f"Objetosc graniastoslupa o podstawie trojkata: {Objetosc_graniastoslupa_o_podstawie_trojkata():.2f}")
elif wybor == "4":
    print(f"Objetosc graniastoslupa o podstawie trapezu: {Objetosc_graniastolupa_o_podstawie_trapezu():.2f}")
elif wybor == "5":
    print(f"Objetosc ostroslupa o podstawie prostokata: {Objetosc_ostroslupa_o_podstawie_prostokata():.2f}")
elif wybor == "6":
    print(f"Objetosc ostroslupa o podstawie trojkata: {Objetosc_ostroslupa_o_podstawie_trojkata():.2f}")
elif wybor == "7":
    print(f"Objetosc kuli: {Objetosc_kuli():.2f}")
elif wybor == "8":
    print(f"Objetosc stozka: {Objetosc_stozka():.2f}")
elif wybor == "9":
    print(f"Objetosc walca: {Objetosc_walca():.2f}")
    
else:
    print("Nieprawidłowy wybór. Spróbuj ponownie.")
 

























