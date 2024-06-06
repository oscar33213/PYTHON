def Dividenum():
    try:
        op1 = (float(input("Primer numero: ")))
        op2 = (float(input("Segundo numero: ")))
    
        print(f"El resultado de la división entre {op1} y {op2} es: " + str(op1/op2))
    except ValueError:
        print("Valor erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    
    finally:
        print("Calculo finalizado")
#ESTE BLOQUE SE EJECUTARA AUNQ OCURRA LA EXCEPCION O NO

Dividenum()


#SE PUEDEN CONCATENAR VARIOS EXCEPTS A UN MISMO TRY
#SE PUEDE OMITIR EL BLOQUE EXCEPT CON EL FINALLY, EL RESULTADO ARROJAR LA EXCEPCION, PERO EJECUTARA EL BLOQUE FINALLY

