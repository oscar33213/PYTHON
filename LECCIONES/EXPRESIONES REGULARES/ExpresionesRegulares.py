import re
#ANCLA
lista_nombres = ['Ana', 'Juan', 'Sandor', 'Lucas', 'Santiago']


for nombres in lista_nombres:
    
    if re.findall('^S', nombres):
        print(nombres)
        

for nombres in lista_nombres:
    
    if re.findall('[oa]', nombres):
        print(nombres)
        
#RANGOS

for nombres in lista_nombres:
    
    if re.findall('[a-d]', nombres): #EN ORDEN ALFEBETICO
        print(nombres)
        
for nombres in lista_nombres:
    
    if re.findall('Sa[^n-r]', nombres): #EN ORDEN ALFEBETICO
        print(nombres)







        




