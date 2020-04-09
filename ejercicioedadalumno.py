edadalum=0
cantalu=0
cantedad=0
prom=0
continuar= 'si'
while continuar == 'si':
    edadalum=float(input("digite edad"))

    if edadalum < 18:
        cantalu=cantalu+1
        cantedad=cantedad+edadalum
        prom=cantedad/cantalu
    elif edadalum >= 18:

        cantalu=cantalu+1
        cantedad=cantedad+edadalum
        prom=cantedad/cantalu

        continuar=input("digite si si quiere continuar")
else:

    print(cantalu)
    print(cantedad)
    print(prom)

