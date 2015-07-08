# arithmetic operations

#fn toswap
def swap(x,y):
    z=x
    x=y
    y=z
    return x,y


#main
print('Enter A:')
a=int(input())

print('Enter B:')
b=int(input())

print('A: ',a)
print('B: ',b)

print('Addition: ',a+b)
print('Subtraction: ',a-b)
print('Multiplication: ',a*b)
print('Division: ',a/b)
print('Remainder: ',a%b)
print('swapping a,b: ')
a,b=swap(a,b)

print('A: ', a)
print('B: ', b)

