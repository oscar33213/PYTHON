import doctest


def area_triangulo(base, altura): 
        
    """TESTEAMOS LA FUNCION
    >>> area_triangulo(3,6)
    9.0'
    
    
    >>> area_triangulo(4,4)
    9.0'
    
    
    >>> area_triangulo(6,2)
    9.0'
    """
        
    return (base * altura)/2



def compruebaMail(mail):
    
    """ 
    Esta función evalua un mail recibido
    >>> compruebaMail(oscar@lopez.com)
    True
    >>> compruebaMail(oscarhidalgo.es)
    False
    >>> compruebaMail(oscarhidalgo.es@)
    """

    arroba  = mail.count('@')
    
    
    if arroba !=1 or mail.rfinf('@') == (len(mail) - 1) or mail.find('@' == 0):
        return False
    else:
        True




doctest.testmod()




