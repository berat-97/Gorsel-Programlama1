sayac = 0
for sayi in range (100,1000):
    sayiS=str(sayi)
    sayiYuzlerBasamagi = sayiS[0]
    sayiOnlarBasamagi = sayiS[1]
    sayiBirlerBasamagi = sayiS[2]
    if(sayiYuzlerBasamagi==sayiOnlarBasamagi or sayiOnlarBasamagi==sayiBirlerBasamagi or sayiBirlerBasamagi==sayiYuzlerBasamagi):
        continue
    else:
        sayac=sayac+1
    
print(sayac)