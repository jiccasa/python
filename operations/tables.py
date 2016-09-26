#tables

print("Enter Table Number To Start with:")
tableFrom=int(input())

print("Enter Table To End with:")
tableEnd=int(input())

for i in range(tableFrom,tableEnd+1,1):
    print("\nMULTIPLICATION TABLE :",i,"\n") 
    for j in range(0,20,1):
        print(i,"X",j,"=",i*j)
