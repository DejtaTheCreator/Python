
import math

print("Witaj w programie obliczajacym pola figur!")



def kwadrat():
    a = int(input("Podaj bok kwadratu"))
    if a>0:
       return a**2
    else:
        return("Boki kwadratu nie mogą byc ujemne ani rowne 0")

def prostokat():
    a = int(input("Podaj 1 bok prostokatu: "))
    b = int(input("Podaj 2 bok prostokatu: "))
    if a>0 and b>0:
        return a*b
    else:
        return("Boki prostokatu nie moga byc ujemne ani rowne 0")
    
def trojkat():
    a = int(input("Podaj bok trojkata: "))
    h = int(input("Podaj wysokosc trojkata padajaca na podany bok: "))
    if a>0 and h>0:
        return a*h/2
    else:
        return("Ani bok ani wysokosc trojkata nie moga byc ujemna ani rowna 0")
    
def trapez():
    a = int(input("Podaj 1 bok trapezu: "))
    b = int(input("Podaj 2 bok trapezu: "))
    h = int(input("Podaj wysokosc trapezu:  "))
    if a>0 and b>0 and h>0:
        return (a+b)*h/2
    else:
        return("Boki ani wysokosc trapezu nie moga byc mniejsze lub rowne 0")

