

#CONTINUE

#SALTA A LA SIGUIENTE INTRUCCION AUN CUANDO EL BUCLE NO A FINALIZADO
for letra in "Hola":
    if letra == "o":
        continue
    #EL BUCLE ENTRARIA EN EL CARACTER ELEGIDO, AUTOMATICAMENTE SALTARA A LA SIGUIENTE INSTRUCCION, EN ESTE CASO NO IMPRIMIRIA LA O
    
    print(f"Viendo la letra {letra}")


contador = 0
nombre = "Oscar Hidalgo"
for i in nombre:
    if i == " ":
        continue
    contador += 1
    
print (contador)


#PASS DEVUELVE NULL A UN BUCLE

class Miclase:
    pass


#ELSE 

email = input("Indica email: ")

for i in email:
    if i == '@':
        arroba = True
        
        break
    

else:
    arroba = False
    


print(arroba)
print(f"Tu email es: {email}")
