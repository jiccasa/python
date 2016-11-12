#Xmastree



def xmastree(height):
	symbols = 1
	for i in reversed (range(height)):
		spaces = i
		xmastree_line(spaces,symbols)
		symbols = symbols + 2
	print(' ' * (height-1) + '$')
	

def xmastree_line(spaces,symbols):
	print(' ' * spaces + '$' * symbols)



	

#Main

height_inp=input("How tall would you like the Xmastree to be: ")


xmastree(height_inp)







