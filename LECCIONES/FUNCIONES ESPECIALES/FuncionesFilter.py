#FUNCION FILTER

#VERIFICA QUE LOS ELEMENTOS DE UNA SECUNCIA CUMPLA UNA CONDICION


def num_par(num):
    if num % 2 == 0:
        return True
    
    
    
    
numeros = [17, 14,1,94,200]


print(list(filter(num_par, numeros))) #(print(list(filter(funcionallamar, listaCreadaConLosValores))))




print(list(filter(lambda numero_impar: numero_impar %2 != 0, numeros ))) # < = SE PUEDE HACER CON FUNCION LAMBDA




