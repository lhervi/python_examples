import re, random

def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    a=m.group(1)
    b=m.group(3)
    return m.group(1) + "".join(inner_word) + m.group(3)
    
texto=""

texto=input("Texto: ")
patron=r"(\w)(\w+)(\w)"
while texto!="q":
    
    print(re.sub(patron, repl, texto))

    texto=input("Texto: ")