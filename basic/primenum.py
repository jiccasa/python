#Prime Number

def is_prime(number):
	n = 2
	prime = True
	while n < number:
		remainder = number % n 
		if remainder == 0:
			prime = False
			break
		n = n + 1
	return prime 


#Main

number = input('Enter a number: ')
if is_prime(number):
	print('This number is a prime number')
else:
	print('This number is not a prime number')

end_num = input('Enter a number: ')
for i in range(end_num):
	if is_prime(i):
		print(i)
	

	




		

