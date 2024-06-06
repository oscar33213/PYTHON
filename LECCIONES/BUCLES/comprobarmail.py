arroba = 0
punto = 0
mail = False

indicaMail = input("Introduce tu email: ")

for i in indicaMail:
    if i == '@':
        arroba += 1
    elif i == '.':
        punto += 1

if arroba == 1 and punto >= 1:
    mail = True

if mail:
    print("Acceso permitido")
else:
    print("ERROR!")
