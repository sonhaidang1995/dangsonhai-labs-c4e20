from random import  randint, choice

x = randint(1,10)
y = randint(1,10)
op = choice(['+','-','*','/'])

res = -9999

if op == '+':
    res = x + y
elif op == '-':
    res = x - y
elif op == '*':
    res = x * y
elif op == '/':
    res = x / y

err = randint(-1,1)

display_result = res + err

print('*'*10)
print('{} {} {} = {}'.format(x,op,y,display_result))
print('*'*10)

ans = input("Y/N: ").upper()
if err == 0:
    if ans == 'Y':
        print("Yay")
    else:
        print("You wrong")
else:
    if ans == 'Y':
        print('You wrong')
    else:
        print('Yay')
