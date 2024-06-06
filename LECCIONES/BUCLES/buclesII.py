#TIPO RANGE

for i in range(5):
    print(f"valor de la variable {i}") #CONCATENACION DE VARIABLES
    
    
    
#ESTE BUCLE CREA UN ARRAY CON 5 NUMEROS, PERO RECORRE SUS POSICIONES


for i in range (5,10):
    print(i)
    

#ESTE BUCLE CREA UN ARRAY QUE EMPIEZA EN 5 Y ACABA EN 9


for i in range (5,50,3):
    print(i)
    
#ESTE BUCLE CREA UN ARRAY QUE EMPIEZA EN 5 Y ACABA EN 50, PERO DE 3 EN 3



#FUNCION len
#DEVUELVE LA LONGITUD DE UN STRING

valido = False
email = input("Introduce mail: ")

for i in range(len(email)):
    if email[i] == '@':
        valido = True
        

if valido:
    print(f"El mail {email} es valido")
else:
    print(f"El mail {email} NO es valido")
    
