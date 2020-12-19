import re 



regexReceive = "^(receive)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]"+"/n$"

regexReceive1 = "^(receive)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]"+"/n"+"(send)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]-"+"[0-1]"+"/n$"

regexReceive2 = "^(receive)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]$"

regexReceive3 = "^(receive)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]"+"/n"

regexSend = "^(send)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]-"+"[0-1]"+"/n$"

regexSend1 = "^(send)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]-"+"[0-1]"+"/n"+"(receive)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]""/n$"

regexSend2 = "^(send)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]-"+"[0-1]$"

regexSend3 = "^(send)-"+"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"+"-[1-4]-"+"[0-1]-"+"[0-1]"+"/n"

sinyalSeviyesiR=""
cihazTuruR=""
sinyalSeviyesiM=""
cihazDurumuR=""

sinyalSeviyesiS=""
cihazTuruS=""
sinyalSeviyesiMS=""
cihazDurumuS=""
cevapS=""
a=0
b=0
c=0
d=0


mesaj = input("mesaj giriniz:")


	

def kontrolet(mesajj): 
        

	global sinyalSeviyesiR
	global sinyalSeviyesiM
	global cihazTuruR
	global cihazDurumuR
	global sinyalSeviyesiS
	global cihazTuruS
	global sinyalSeviyesiMS
	global cihazDurumuS
	global cevapS
	global a
	global b
	global c
	global d
	

	
	if(re.search(regexReceive2,mesajj)): 
               print("İkinci bölüm hatalı")
               a=a+1;
               mesaj=input("mesaj giriniz:")
               kontrolet(mesaj)
                       
                      
               
	if(re.search(regexSend2,mesajj)): 
               print("İkinci bölüm hatalı")
               a=a+1;
               mesaj=input("mesaj giriniz:")
               kontrolet(mesaj)
	
	
	
	if(len(mesajj)==17): 
                
                mesajj=mesajj[:15]+"/"+mesajj[16:]
                
	if(len(mesajj)==16): 
                
                mesajj=mesajj[:14]+"/"+mesajj[15:]      

	if(len(mesajj)==15): 
               
                mesajj=mesajj[:13]+"/"+mesajj[14:]

	if(len(mesajj)==14): 
                
                mesajj=mesajj[:12]+"/"+mesajj[13:]
                
	if(len(mesajj)>17 and mesajj[0]=="r"): 
                
                nIndex = mesajj.find('n',mesajj.find('n')+0)
                mesajj=mesajj[:(nIndex-1)]+"/"+mesajj[nIndex:(len(mesajj)-2)]+"/n"
               

	if(len(mesajj)>17 and mesajj[0]=="s"): 
               
                nIndex = mesajj.find('n',mesajj.find('n')+1)
                mesajj=mesajj[:(nIndex-1)]+"/"+mesajj[nIndex:(len(mesajj)-2)]+"/n"
                
	               
                
                
                
	if(re.search(regexReceive3,mesajj[0:17]) or re.search(regexReceive3,mesajj[0:16]) or re.search(regexReceive3,mesajj[0:15])): 
	        a=25
	        
	else:
	        a=50


	if(re.search(regexReceive1,mesajj)): 
	        b=25
	        
	else:
	        b=50
                
                
	if(re.search(regexSend3,mesajj[0:16]) or re.search(regexSend3,mesajj[0:15]) or re.search(regexSend3,mesajj[0:14])): 
	        c=25
	    
	else:
	        c=50


	if(re.search(regexSend,mesajj)): 
	        d=25
	        
	else:
	        d=50

	
	
	if(re.search(regexReceive,mesajj)): 
	
		
		if (mesajj[11]=="-" and mesajj[9]!="-"):
		    
		    
		    sinyalSeviyesiR = mesajj[8:11]
		    
		    sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		    if (sinyalSeviyesiRi<50):
		       
		        sinyalSeviyesiM = "Çok Zayıf"
		        
		    if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		        sinyalSeviyesiM = "Zayıf"
		        
		    if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		        sinyalSeviyesiM = "Orta"
		        
		    if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		        sinyalSeviyesiM = "Güçlü"
		        
		    if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		        sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		    if(mesajj[12]=="1"):
		    
		        cihazTuruR="Televizyon"
		        
		    if(mesajj[12]=="2"):
		    
		        cihazTuruR="Çamaşır Makinesi"
		        
		    if(mesajj[12]=="3"):
		    
		        cihazTuruR="Buz Dolabi"
		        
		    if(mesajj[12]=="4"):
		    
		        cihazTuruR="Firin"
		        
		    if (mesajj[14]=="0"):
		        
		        cihazDurumuR="Off"
		        
		    else:
		        cihazDurumuR="On"
		    print("Kod Tipi : receive - Gelen")	
		    print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		    print("Cihaz :"+mesajj[12]+" ",cihazTuruR)
		    print("Durumu :"+mesajj[14]+" ",cihazDurumuR)
		        
		
		if (mesajj[10]=="-"):
		
		    sinyalSeviyesiR = mesajj[8:10]
		    

		    
		    sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		    if (sinyalSeviyesiRi<50):
		       
		        sinyalSeviyesiM = "Çok Zayıf"
		        
		    if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		        sinyalSeviyesiM = "Zayıf"
		        
		    if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		        sinyalSeviyesiM = "Orta"
		        
		    if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		        sinyalSeviyesiM = "Güçlü"
		        
		    if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		        sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		    if(mesajj[11]=="1"):
		    
		        cihazTuruR="Televizyon"
		        
		    if(mesajj[11]=="2"):
		    
		        cihazTuruR="Çamaşır Makinesi"
		        
		    if(mesajj[11]=="3"):
		    
		        cihazTuruR="Buz Dolabi"
		        
		    if(mesajj[11]=="4"):
		    
		        cihazTuruR="Firin"
		        
		    if (mesajj[13]=="0"):
		        
		        cihazDurumuR="Off"
		        
		    else:
		        cihazDurumuR="On"
		    print("Kod Tipi : receive - Gelen")	
		    print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		    print("Cihaz :"+mesajj[11]+" ",cihazTuruR)
		    print("Durumu :"+mesajj[13]+" ",cihazDurumuR)
		    
		
		if (mesajj[9]=="-"):
		
		    sinyalSeviyesiR = mesajj[8:9]
		    
		   
		    
		    sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		    if (sinyalSeviyesiRi<50):
		       
		        sinyalSeviyesiM = "Çok Zayıf"
		        
		    if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		        sinyalSeviyesiM = "Zayıf"
		        
		    if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		        sinyalSeviyesiM = "Orta"
		        
		    if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		        sinyalSeviyesiM = "Güçlü"
		        
		    if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		        sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		    if(mesajj[10]=="1"):
		    
		        cihazTuruR="Televizyon"
		        
		    if(mesajj[10]=="2"):
		    
		        cihazTuruR="Çamaşır Makinesi"
		        
		    if(mesajj[10]=="3"):
		    
		        cihazTuruR="Buz Dolabi"
		        
		    if(mesajj[10]=="4"):
		    
		        cihazTuruR="Firin"
		        
		    if (mesajj[12]=="0"):
		        
		        cihazDurumuR="Off"
		        
		    else:
		        cihazDurumuR="On"
		    print("Kod Tipi : receive - Gelen")	
		    print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		    print("Cihaz :"+mesajj[10]+" ",cihazTuruR)
		    print("Durumu :"+mesajj[12]+" ",cihazDurumuR)
		

        
		mesaj = input("mesaj giriniz:")
		kontrolet(mesaj)  
		
	elif(re.search(regexSend,mesajj)): 
		
		
		if (mesajj[8]=="-" and mesajj[6]!="-"):
		    
		    
		    sinyalSeviyesiS = mesajj[5:8]
		    
		    sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		    if (sinyalSeviyesiSi<50):
		       
		        sinyalSeviyesiMS = "Çok Zayıf"
		        
		    if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		        sinyalSeviyesiMS = "Zayıf"
		        
		    if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		        sinyalSeviyesiMS = "Orta"
		        
		    if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		        sinyalSeviyesiMS ="Güçlü"
		        
		    if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		        sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		    if(mesajj[9]=="1"):
		    
		        cihazTuruS="Televizyon"
		        
		    if(mesajj[9]=="2"):
		    
		        cihazTuruS="Çamaşır Makinesi"
		        
		    if(mesajj[9]=="3"):
		    
		        cihazTuruS="Buz Dolabi"
		        
		    if(mesajj[9]=="4"):
		    
		        cihazTuruS="Firin"
		        
		    if (mesajj[11]=="0"):
		        
		        cihazDurumuS="Off"
		        
		    else:
		        cihazDurumuS="On"
               
               
		    if (mesajj[13]=="0"):
		        
		        cevapS="İstenmiyor"
		        
		    else:
		        cevapS="İsteniyor"

		    print("Kod Tipi : send - Giden")	
		    print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		    print("Cihaz :"+mesajj[9]+" ",cihazTuruS)
		    print("Durumu :"+mesajj[11]+" ",cihazDurumuS)
		    print("Cevap :"+mesajj[13]+" ",cevapS)
		    
		if (mesajj[7]=="-"):
		    
		    
		    sinyalSeviyesiS = mesajj[5:7]
		    
		    sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		    if (sinyalSeviyesiSi<50):
		       
		        sinyalSeviyesiMS = "Çok Zayıf"
		        
		    if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		        sinyalSeviyesiMS = "Zayıf"
		        
		    if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		        sinyalSeviyesiMS = "Orta"
		        
		    if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		        sinyalSeviyesiMS ="Güçlü"
		        
		    if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		        sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		    if(mesajj[8]=="1"):
		    
		        cihazTuruS="Televizyon"
		        
		    if(mesajj[8]=="2"):
		    
		        cihazTuruS="Çamaşır Makinesi"
		        
		    if(mesajj[8]=="3"):
		    
		        cihazTuruS="Buz Dolabi"
		        
		    if(mesajj[8]=="4"):
		    
		        cihazTuruS="Firin"
		        
		    if (mesajj[10]=="0"):
		        
		        cihazDurumuS="Off"
		        
		    else:
		        cihazDurumuS="On"
               
               
		    if (mesajj[12]=="0"):
		        
		        cevapS="İstenmiyor"
		        
		    else:
		        cevapS="İsteniyor"

		    print("Kod Tipi : send - Giden")	
		    print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		    print("Cihaz :"+mesajj[8]+" ",cihazTuruS)
		    print("Durumu :"+mesajj[10]+" ",cihazDurumuS)
		    print("Cevap :"+mesajj[12]+" ",cevapS)
		    
                		    
		if (mesajj[6]=="-"):
		    
		    
		    sinyalSeviyesiS = mesajj[5:6]
		    
		    sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		    if (sinyalSeviyesiSi<50):
		       
		        sinyalSeviyesiMS = "Çok Zayıf"
		        
		    if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		        sinyalSeviyesiMS = "Zayıf"
		        
		    if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		        sinyalSeviyesiMS = "Orta"
		        
		    if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		        sinyalSeviyesiMS ="Güçlü"
		        
		    if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		        sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		    if(mesajj[7]=="1"):
		    
		        cihazTuruS="Televizyon"
		        
		    if(mesajj[7]=="2"):
		    
		        cihazTuruS="Çamaşır Makinesi"
		        
		    if(mesajj[7]=="3"):
		    
		        cihazTuruS="Buz Dolabi"
		        
		    if(mesajj[7]=="4"):
		    
		        cihazTuruS="Firin"
		        
		    if (mesajj[9]=="0"):
		        
		        cihazDurumuS="Off"
		        
		    else:
		        cihazDurumuS="On"
               
               
		    if (mesajj[11]=="0"):
		        
		        cevapS="İstenmiyor"
		        
		    else:
		        cevapS="İsteniyor"

		    print("Kod Tipi : send - Giden")	
		    print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		    print("Cihaz :"+mesajj[7]+" ",cihazTuruS)
		    print("Durumu :"+mesajj[9]+" ",cihazDurumuS)
		    print("Cevap :"+mesajj[11]+" ",cevapS)
		    
		mesaj = input("mesaj giriniz:")
		kontrolet(mesaj) 
		
	elif(re.search(regexSend1,mesajj)): 
		
		

		sIndex1 = mesajj.find('-',mesajj.find('-')+0)
                
		sIndex2 = mesajj.find('-',mesajj.find('-')+1)
		
		if (sIndex2-sIndex1 == 4):
		        
		        sinyalSeviyesiS = mesajj[5:8]
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		        
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS = "Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"

		        if(mesajj[9]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[9]=="2"):  
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[9]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[9]=="4"):
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[11]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
		                
		        if (mesajj[13]=="0"):
		        
		                cevapS="Off"
		        
		        else:
		                cevapS="On"		                
		                
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)    
		        print("Cihaz :"+mesajj[sIndex2+1]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[sIndex2+3]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[sIndex2+5]+" ",cevapS)
		        

		if (sIndex2-sIndex1 == 3):
		        
		        sinyalSeviyesiS = mesajj[5:7]
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		        
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS = "Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"

		        if(mesajj[8]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[8]=="2"):  
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[8]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[8]=="4"):
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[10]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
		                
		        if (mesajj[12]=="0"):
		        
		                cevapS="Off"
		        
		        else:
		                cevapS="On"		                
		                
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)    
		        print("Cihaz :"+mesajj[sIndex2+1]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[sIndex2+3]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[sIndex2+5]+" ",cevapS)
		        
		if (sIndex2-sIndex1 == 2):
		        
		        sinyalSeviyesiS = mesajj[5:6]
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		        
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS = "Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"

		        if(mesajj[7]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[7]=="2"):  
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[7]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[7]=="4"):   
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[9]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
		                
		        if (mesajj[11]=="0"):
		        
		                cevapS="Off"
		        
		        else:
		                cevapS="On"		                
		                
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)    
		        print("Cihaz :"+mesajj[sIndex2+1]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[sIndex2+3]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[sIndex2+5]+" ",cevapS)
		        
		        
		        
		print ("--------------")  		        
		
	                   
		
		if (len(mesajj)-mesajj.find('r')==17):		
		        sinyalSeviyesiR = mesajj[sIndex2+16:sIndex2+19]
		     
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM ="Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[sIndex2+20]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[sIndex2+20]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[sIndex2+20]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[sIndex2+20]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[sIndex2+22]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
               
		                
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[sIndex2+20]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[sIndex2+22]+" ",cihazDurumuR)

		
		if (len(mesajj)-mesajj.find('r')==16):		
		        sinyalSeviyesiR = mesajj[sIndex2+16:sIndex2+18]
		     
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM ="Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[sIndex2+19]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[sIndex2+19]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[sIndex2+19]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[sIndex2+19]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[sIndex2+21]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
               
		                
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[sIndex2+19]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[sIndex2+21]+" ",cihazDurumuR)
		        
		
		if (len(mesajj)-mesajj.find('r')==15):		
		        sinyalSeviyesiR = mesajj[sIndex2+16:sIndex2+17]
		     
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM ="Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[sIndex2+18]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[sIndex2+18]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[sIndex2+18]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[sIndex2+18]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[sIndex2+20]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
               
		                
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[sIndex2+19]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[sIndex2+21]+" ",cihazDurumuR)

		        

		mesaj = input("mesaj giriniz:")		
		kontrolet(mesaj) 
		
	elif(re.search(regexReceive1,mesajj)): 
		
		
		nIndex1 = mesajj.find('-',mesajj.find('-')+0)
                
		nIndex2 = mesajj.find('-',mesajj.find('-')+1)

		
		
               
		if (nIndex2-nIndex1 == 4):
		     
		   
		        sinyalSeviyesiR = mesajj[8:11]
		        
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM = "Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[12]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[12]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[12]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[12]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[14]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[12]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[14]+" ",cihazDurumuR)
		        
		        
		        

		       

		if (nIndex2-nIndex1 == 3):
		    
		        sinyalSeviyesiR = mesajj[8:10]
		        
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM = "Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[11]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[11]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[11]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[11]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[13]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[11]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[13]+" ",cihazDurumuR)
                
		if (nIndex2-nIndex1 == 2):
		      
		       
		        sinyalSeviyesiR = mesajj[8:9]
		        
		        sinyalSeviyesiRi=int(sinyalSeviyesiR)
		    
		        if (sinyalSeviyesiRi<50):
		       
		                sinyalSeviyesiM = "Çok Zayıf"
		        
		        if (sinyalSeviyesiRi>49 and sinyalSeviyesiRi<100):
		        
		                sinyalSeviyesiM = "Zayıf"
		        
		        if (sinyalSeviyesiRi>99 and sinyalSeviyesiRi<150):
		            
		        
		                sinyalSeviyesiM = "Orta"
		        
		        if (sinyalSeviyesiRi>149 and sinyalSeviyesiRi<200):
		       
		                sinyalSeviyesiM = "Güçlü"
		        
		        if (sinyalSeviyesiRi>199 and sinyalSeviyesiRi<256):
		        
		                sinyalSeviyesiM = "Çok Güçlü"
		       
		        
		        if(mesajj[10]=="1"):
		    
		                cihazTuruR="Televizyon"
		        
		        if(mesajj[10]=="2"):
		    
		                cihazTuruR="Çamaşır Makinesi"
		        
		        if(mesajj[10]=="3"):
		    
		                cihazTuruR="Buz Dolabi"
		        
		        if(mesajj[10]=="4"):
		    
		                cihazTuruR="Firin"
		        
		        if (mesajj[12]=="0"):
		        
		                cihazDurumuR="Off"
		        
		        else:
		                cihazDurumuR="On"
		        print("Kod Tipi : receive - Gelen")	
		        print("Sinyal Gucu :"+sinyalSeviyesiR+" - ",sinyalSeviyesiM)
		        print("Cihaz :"+mesajj[10]+" ",cihazTuruR)
		        print("Durumu :"+mesajj[12]+" ",cihazDurumuR)
		        
		 
                
		print ("--------------")  
		
		
		nIndex3 = mesajj.find('d')
                
		nIndex4 = len(mesajj)
		

		if (nIndex4-nIndex3 == 13):
		   
		    
		        sinyalSeviyesiS = mesajj[nIndex2+11:nIndex2+14]
		     
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS ="Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		        if(mesajj[nIndex2+15]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[nIndex2+15]=="2"):
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[nIndex2+15]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[nIndex2+15]=="4"):
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[nIndex2+17]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
               
               
		        if (mesajj[nIndex2+19]=="0"):
		        
		                cevapS="İstenmiyor"
		        
		        else:
		                cevapS="İsteniyor"
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		        print("Cihaz :"+mesajj[nIndex2+15]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[nIndex2+17]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[nIndex2+19]+" ",cevapS)

		if (nIndex4-nIndex3 == 12):
		   
		    
		        sinyalSeviyesiS = mesajj[nIndex2+11:nIndex2+13]
		     
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS ="Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		        if(mesajj[nIndex2+14]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[nIndex2+14]=="2"):
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[nIndex2+14]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[nIndex2+14]=="4"):
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[nIndex2+16]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
               
               
		        if (mesajj[nIndex2+18]=="0"):
		        
		                cevapS="İstenmiyor"
		        
		        else:
		                cevapS="İsteniyor"
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		        print("Cihaz :"+mesajj[nIndex2+14]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[nIndex2+16]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[nIndex2+18]+" ",cevapS)
                	
		if (nIndex4-nIndex3 == 11):
		   
		    
		        sinyalSeviyesiS = mesajj[nIndex2+11:nIndex2+12]
		     
		        sinyalSeviyesiSi=int(sinyalSeviyesiS)
		    
		        if (sinyalSeviyesiSi<50):
		       
		                sinyalSeviyesiMS = "Çok Zayıf"
		        
		        if (sinyalSeviyesiSi>49 and sinyalSeviyesiSi<100):
		        
		                sinyalSeviyesiMS = "Zayıf"
		        
		        if (sinyalSeviyesiSi>99 and sinyalSeviyesiSi<150):
		            
		        
		                sinyalSeviyesiMS = "Orta"
		        
		        if (sinyalSeviyesiSi>149 and sinyalSeviyesiSi<200):
		       
		                sinyalSeviyesiMS ="Güçlü"
		        
		        if (sinyalSeviyesiSi>199 and sinyalSeviyesiSi<256):
		        
		                sinyalSeviyesiMS = "Çok Güçlü"
		       
		        
		        if(mesajj[nIndex2+13]=="1"):
		    
		                cihazTuruS="Televizyon"
		        
		        if(mesajj[nIndex2+13]=="2"):
		    
		                cihazTuruS="Çamaşır Makinesi"
		        
		        if(mesajj[nIndex2+13]=="3"):
		    
		                cihazTuruS="Buz Dolabi"
		        
		        if(mesajj[nIndex2+13]=="4"):
		    
		                cihazTuruS="Firin"
		        
		        if (mesajj[nIndex2+15]=="0"):
		        
		                cihazDurumuS="Off"
		        
		        else:
		                cihazDurumuS="On"
               
               
		        if (mesajj[nIndex2+17]=="0"):
		        
		                cevapS="İstenmiyor"
		        
		        else:
		                cevapS="İsteniyor"
		        print("Kod Tipi : send - Giden")	
		        print("Sinyal Gucu :"+sinyalSeviyesiS+" - ",sinyalSeviyesiMS)
		        print("Cihaz :"+mesajj[nIndex2+13]+" ",cihazTuruS)
		        print("Durumu :"+mesajj[nIndex2+15]+" ",cihazDurumuS)
		        print("Cevap :"+mesajj[nIndex2+17]+" ",cevapS)
                
                
                
                

		mesaj = input("mesaj giriniz:")
		kontrolet(mesaj) 

	elif(a==25 and b==50):
	        
               print("İkinci bölüm hatalı")
               print("-------------------")
               print("send veya receive içermiyor")               
               mesaj=input("mesaj giriniz:")
               kontrolet(mesaj)
		
	elif(c==25 and d==50):
	        
               print("İkinci bölüm hatalı")
               print("-------------------")
               print("send veya receive içermiyor")               
               mesaj=input("mesaj giriniz:")
               kontrolet(mesaj)		
	else: 
               print("Mesaj Hatalı")
               mesaj=input("mesaj giriniz:")
               kontrolet(mesaj)

		

		
		
	
kontrolet(mesaj) 

