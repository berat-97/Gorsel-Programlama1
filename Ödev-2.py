import re 

regex = ("www."+"[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")


url = input("URL giriniz:")

def kontrolet(urll): 

	if(re.search(regex,urll)): 
		print("Girilen url Adresi Doğru") 
		url = input("URL giriniz:")
		kontrolet(url) 
		
	else: 
		print("Girilen url Adresi Yanlış") 
		url = input("URL giriniz:")
		kontrolet(url) 
		
	
kontrolet(url) 