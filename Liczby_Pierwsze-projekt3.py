
print("Witaj w prgoramie sprawdzającym czy dana liczba jest pierwsza!")


while True:
    a = int(input("Podaj liczbę: "))
    for i in range(2,a):
        if a % i == 0:
            print("Podana liczba nie jest pierwsza")
            break
    else:
        print("Podana liczba jest pierwsza")




