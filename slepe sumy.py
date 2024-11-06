

n=int(input("Podaj n -  "))
suma=0
for i in range(1, n+1):
    suma+=i
print(suma)

def suma_rekurencyjna(n):
    if n==0:
        return 0
    return n+suma_rekurencyjna(n-1)

print(suma_rekurencyjna(n))
