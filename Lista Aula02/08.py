"""
P = True e Q = False. Aplique De Morgan na seguinte proposição e atribua o valor a uma
variável - ~(p ^ (p v q)), essa variável deve ser retornada partir de uma função
"""
p = True
q = False
print(not(p and(p or q)))