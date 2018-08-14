# Khai báo function
def cacl(x, y, op):
    
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
     
# Thực thi function
result = cacl(3, 7, "-")
print(result)