#KALKULATOR

print("Witaj w Kalkulatorze!")

a=int(input("Podaj pierwsza liczbe: "))
b=input("Podaj typ dzialania: ")
c=int(input("Podaj druga liczbe: "))


if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
if b=="/" and c==0:
    print("Nie dziel przez 0 ")
elif b=="/":
    print(a/c)
if b=="%" and c==0:
    print("Nie dziel przez 0 ")
elif b=="%":
    print(a%c)
elif b=="**":
    print(a**c)