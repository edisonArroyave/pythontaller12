numero=1
cantnume=0
cantnumeronega=0
while numero !=0:
    numero=float(input("digite numero"))
    if numero >0:
      cantnume=cantnume+1
    elif numero < 0:
        cantnumeronega=cantnumeronega+1
else:      
      print(cantnume)
      print(cantnumeronega)