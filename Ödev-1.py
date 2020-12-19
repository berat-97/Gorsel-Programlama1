import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


emailadres = input("Email giriniz:")

def kontrolet(email): 


	if(re.search(regex,email)): 
		print("Girilen E-mail Adresi Doğru") 
		emailadres = input("Email giriniz:")
		kontrolet(emailadres) 
		
	else: 
		print("Girilen E-mail Adresi Yanlış") 
		emailadres = input("Email giriniz:")
		kontrolet(emailadres) 
		
	
kontrolet(emailadres) 