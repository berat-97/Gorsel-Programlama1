metin = input("Metini Girin: ")
aranan = input("Aranan Metini Girin: ")
arananIndex = metin.find(aranan) 
arananUzunluk = len(aranan)

print (metin[arananIndex-1]+aranan+metin[arananIndex+arananUzunluk])