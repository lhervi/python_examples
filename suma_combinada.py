import re

def suma_combinada(lista1, lista2=[0]):    
    suma = []
    for i in lista1:
        for j in lista2:
            suma.append(i+j)
    return suma

patron=r'\b([1-7])\b\s{1}\b(1000|[0-9]{1,3})\b'

def modulo_max(lista, mod):

    prov=list(map(lambda x: x%mod, lista))
    prov.sort(reverse=True)
    return prov[0]

inicio = str(input())
if re.match(patron, inicio):
    lista=[]
    listas=[]
    lista_final=[0]
    prov=inicio.split(' ')
    n_listas=int(prov[0])
    mod=int(prov[1])

    for i in range(n_listas):
        prov=str(input())
        prov=prov.split()
        prov=list(map(lambda x: int(x)**2, prov))
        listas.append(prov)

    for lista in listas:
        lista_final=suma_combinada(lista[1:], lista_final)
        
    mod_max=modulo_max(lista_final, mod)
   
    print(mod_max)


    






























