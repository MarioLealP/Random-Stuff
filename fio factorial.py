def tulostaLuvunKertoma(n):
    print(str(n) +  "! =", laskeKertoma(n))

def lueKokonaisLuku():
    while True:
        n = input("Anna kokonaisluku: ")
        try:
            return int(n)
            break
        except ValueError:
            print("Virheellinen syöte.")

def laskeKertoma(n):
    kertoma = 1
    for laskuri in range(1,n+1):
        kertoma *= laskuri
    return kertoma

#pääohjelma
while True:
    n = lueKokonaisLuku()
    if n >= 0:
        tulostaLuvunKertoma(n)
    else:
        break
print("Ohjelma lopetetaan.")