"""Escreva três funções que gerem automaticamente dicionários com dic comprehensions. Em seguida utilize essas funções como argumentos de outra função que irá recebê-las e retornar um único dicionário ."""

def d1(a): 
    a = {x :x for x in range(0,11)}
    #print(a) 
    return a  
#d1("a")
def d2(b): 
    b = {x :x for x in range(11,21)}
    #print(b) 
    return b  
#d2("b")
def d3(c): 
    c = {x :x for x in range(21,31)}
    #print(c)
    return c 
#d3("c")  

def junta_d(d1, d2, d3):
    d1.update(d2)
    d1.update(d3)
    print(d1)
junta_d(d1('a'), d2('b'), d3('c'))




