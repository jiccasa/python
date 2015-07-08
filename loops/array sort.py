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

print ("Before Sort: ", x)
x.sort()
print ("After Sort: ", x)

