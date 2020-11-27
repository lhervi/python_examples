import re

def eval2(cod):
    
    pat2=r"(\d)(?=\d\1)"

    resultado2=re.findall(pat2,cod)
    
    return resultado2

def eval1(cod):
    pat1 = r"(^[1-9]\d{5}$)"    
    c1 = re.compile(pat1)
    resultado1 = c1.match(cod)   
    return resultado1

cod=str(input("Codigo: "))

while cod != "q":
    print(eval1(cod))
    res=eval2(cod)
    print(res)
    print("Len de res ", len(res))
    print(type(res))
    
    print(len(re.findall("\d\d", str(re.findall(r"(\d\d)(\1)",cod)))))
    
    cod = input("Codigo: ")

