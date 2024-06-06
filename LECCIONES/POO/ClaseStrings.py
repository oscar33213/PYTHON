

edad = input("Indica tu edad: ")
while (edad.isdigit()==False):
    print("Porfavor, introduce un valor numerico")
    
    edad = input("Indica tu edad: ")
    
    
if(int(edad)>= 18):
    print("Puedes pasar")
else:
    print("No puedes pasar")
    



