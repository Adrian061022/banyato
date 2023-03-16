# 1. feladat
# Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
# meg a következő feladatokat!

melysegek=[]

with open("./banyato/melyseg.txt","r",encoding="utf-8") as fin:
    fin.readline()
    fin.readline()
    for sor in fin:
        seged_lista=list(map(int,sor.strip().split()))
        print(seged_lista)
        melysegek.append(seged_lista)

# print(melysegek)

from colorama import Fore, Back

for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}", end=" ")
        else:
             print(f"{Back.RESET}{Fore.BLACK}{melyseg:2d}", end=" ")
    print()
