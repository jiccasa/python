#multtables

tablefrom=input("What table do you want to start from? ")
tablend=input("What table do you want to end at? ")


for i in range(tablefrom,tablend+1,1):
	print("Table : " + str(i))
	for j in range(0,21,1):
		print(str(i)+ " * "+  str(j) + " = " + str(i*j))