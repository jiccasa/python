# Basic Mathematical operations

#fn tocalculateremainder
def remainder(x,y):
    return(x%y)


# Main

a = input("Enter A: ")
b = input("Enter B: ")



print("Addition: " + str(a)+"+"+str(b)+ ": = "+ str(a+b))
print("Subtraction: " + str(a)+"-"+str(b)+ ": = "+ str(a-b))
print("Multiplication: " + str(a)+"*"+str(b)+ ": = "+ str(a*b))
print("Division: " + str(a)+"/"+str(b)+ ": = "+ str(a/float(b)))
print("Remainder: " + str(a)+"%"+str(b)+ ": = "+ str(a%b))

print("Remainder2: " + str(a)+"%"+str(b)+ ": = "+ str(remainder(a,b)))