

import sys

def add(num1, num2):
    add = num1 + num2
    return add
def sub(num1, num2):
    sub =num1 - num2
    return sub
def mul(num1, num2):
    mul = num1* num2
    return mul
def div(num1, num2):
    div = num1/num2
    return div

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "+":
    print(add(num1,num2))
elif operator == "-":
    print(sub(num1,num2))
elif operator == "*":
    print(mul(num1,num2))
elif operator == "/":
    print(div(num1,num2))
    
else:    print("invalid operator")  
