num1=int(input("informe um valor-> "))
num2=int(input("informe outro valor-> "))
print("operação mul, div, sub, adi")
op=str(input("informe a operação-> "))

if op == adi:
    return num1 + num2

elif op == sub:
    return num1 - num2

elif op == div:
    return num1 / num2

elif op == mul:
    return num1 * num2

else:
    return ("invalido")