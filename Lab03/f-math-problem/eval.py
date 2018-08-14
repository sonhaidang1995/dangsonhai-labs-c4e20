def cacl(x, y, op):
    
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y 

result = cacl(3, 7, "-")
print(result)