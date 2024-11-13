#papier kamien nozyce

import random

 

opcje = ["Paper","Kamien","Nozyce"]

 

wybor_gracza = input("Postaw Papier , Kamien lub Nozyce: ")

wybor_komputera = random.choice(opcje)

print("Komputer postawil: ", wybor_komputera)

if wybor_gracza == wybor_komputera:

    print("Remis")

elif wybor_gracza == "Kamien" and wybor_komputera == "Nozyce":

    print("Brawo , Wygrales!")

elif wybor_gracza == "Papier" and wybor_komputera == "Kamien":

    print("Brawo , Wygrales!")

elif wybor_gracza == "Scissors" and wybor_komputera == "Papier":

    print("Brawo , wygrales!")

else:

    print("Niestety , przegrales nawet z komputerem :/ ")







