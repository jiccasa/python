#arrays

#Method 1
print("How many elements do  you want in you list?")
n=int(input())
x=[0] *n
i=0
while i<n:
    print("Enter element", i)
    x[i]=int(input())
    i=i+1

print(x)

#Method 2
print("How many elements do  you want in you list?")
n=int(input())
x=[]
i=0
while i<n:
    print("Enter element", i)
    e=int(input())
    x.append(e)
    i=i+1

print(x)
    
#Method 3
print("How many elements do  you want in you list?")
n=int(input())
x=[]
for i in range(0,n,1):
    print("Enter element", i)
    e=int(input())
    x.append(e)


print(x)
