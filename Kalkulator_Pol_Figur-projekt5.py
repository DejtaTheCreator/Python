
import math

print("Witaj w programie obliczajacym pola figur!")



def kwadrat():
    a = int(input("Podaj bok kwadratu"))
    if a>0:
       return a**2
    else:
        print("Boki kwadratu nie mogą byc ujemne ani rowne 0")

def prostokat():
    a = int(input("Podaj 1 bok prostokatu: "))
    b = int(input("Podaj 2 bok prostokatu: "))
    if a>0 and b>0:
        return a*b
    else:
        print("Boki prostokatu nie moga byc ujemne ani rowne 0")
    
def trojkat():
    a = int(input("Podaj bok trojkata: "))
    h = int(input("Podaj wysokosc trojkata padajaca na podany bok: "))
    if a>0 and h>0:
        return a*h/2
    else:
        print("Ani bok ani wysokosc trojkata nie moga byc ujemna ani rowna 0")
    
def trapez():
    a = int(input("Podaj 1 bok trapezu: "))
    b = int(input("Podaj 2 bok trapezu: "))
    h = int(input("Podaj wysokosc trapezu:  "))
    if a>0 and b>0 and h>0:
        return (a+b)*h/2
    else:
        print("Boki ani wysokosc trapezu nie moga byc mniejsze lub rowne 0")

def rownoleglobok():
    a = int(input("Podaj bok rownolegloboku: "))
    h = int(input("Podaj wysokosc rownolegloboku: "))
    if a>0 and h>0:
        return a*h
    else:
        print("Wysokosc ani boki nie moga byc mniejsze lub rowne 0")

def romb():
    e = int(input("Podaj dlugosc 1 przekatnej rombu: "))
    f = int(input("Podaj dlugosc 2 przekatnej rombu: "))
    if e>0 and f>0:
        return e*f/2
    else:
        print("Przekatne rombu nie moga byc mniejsze lub rowne 0")

def kolo():
    r = int(input("Podaj promien kola: "))
    if r>0:
        return math.pi*r**2
    else:
        print("Promien kola nie moze byc mniejszy lub rowny 0")

def szesciakat():
    a = int(input("Podaj dlugosc boku szesciakata foremnego: "))
    if a>0:
        return (3*(a**2)*(math.sqrt(2)))
    else:
        print("Promien kola nie moze byc mniejszy lub rowny 0")


print("1. Pole kwadratu")
print("2. Pole prostokata")
print("3. Pole trojkata")
print("4. Pole trapezu")
print("5. Pole rownolegloboku")
print("6. Pole rombu")
print("7. Pole kola")
print("8. Pole szesciakata foremnego")

wybor = input("Wybierz opcję (1-8): ")
 
if wybor == "1":
    print(f"Pole kwadratu: {kwadrat():.2f}")
elif wybor == "2":
    print(f"Pole prostakata: {prostokat():.2f}")
elif wybor == "3":
    print(f"Pole trojkata: {trojkat():.2f}")
elif wybor == "4":
    print(f"Pole trapezu: {trapez():.2f}")
elif wybor == "5":
    print(f"Pole rownolegloboku: {rownoleglobok():.2f}")
elif wybor == "6":
    print(f"Pole rombu: {romb():.2f}")
elif wybor == "7":
    print(f"Pole kola: {kolo():.2f}")
elif wybor == "8":
    print(f"Pole szesciakata foremnego: {szesciakat():.2f}")
    
else:
    print("Nieprawidłowy wybór. Spróbuj ponownie.")

#KONIEC