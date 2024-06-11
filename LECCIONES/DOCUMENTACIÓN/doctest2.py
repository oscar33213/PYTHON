import math
import doctest

def raiz(lista_numeros):
    
    """LA FUNCION DEVUELVE UNA LISTA CON LA RAIZ CUADRADA
    
    
    >>> lista  = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raiz(lista)
    [2.0, 3.0, 4.0]
    
    
    
    
    
    
    """
    
    
    return [math.sqrt(n) for n in lista_numeros]
    
    
doctest.testmod()

