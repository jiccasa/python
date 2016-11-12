#Fibonacci Sequence


end_num = input('At what number would you like the Fibonacci Sequence to end: ')
f_number = 1
s_number = 1
t_number = f_number + s_number
print(f_number)
print(s_number)
while t_number <= end_num:
	print(t_number)
	f_number = s_number
	s_number = t_number
	t_number = f_number + s_number





