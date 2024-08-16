karakterler  ="+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random

hesap   = input("Hangi  hesabın  için şifre  istiyorsun?\n")
adet =  int(input("Kaç  karakterli şifre  istersin?\n"))


def sifre_olustur(sayi):
    sifre =""
    for i in range(sayi):
        sifre += random.choice(karakterler)
    return sifre

with open("sifrelerim.txt" , "a") as doc:
    
    sifre =  sifre_olustur(adet)
    doc.write(f"{hesap} : {sifre}\n")

print(sifre)

