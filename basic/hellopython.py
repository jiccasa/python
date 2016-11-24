import random
import sys
import os

print("Hello World!")
name = "Jalandar"
print(name)
name = 2
print(name)

print("10 + 5 =", 10+5)
print("10 - 5 =", 10-5)
print("10 * 5 =", 10*5)
print("10 / 5 =", 10/5)
print("10 % 5 =", 10%5)
print("10 ** 5 =", 10**5)
print("10 // 5 =", 10//5)

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

quote = "\"You are a deanzas,"

multi_line_quote = ''' You
are a deanzas" '''
 

name = 15
print(name)

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)
 
print("%s %s %s" % ('You are a deanzas', quote, multi_line_quote))
 
print("I am not a ", end="")
print("deanzas")
 

print('Hello' * 5)
 
 
grocery_list = ['Cookies', 'Cake', 'Strawberries', 'Bananas','Cheetos']
print(grocery_list[0:1])

print('The first item is', grocery_list[0])
 
grocery_list[2] = "Waffles"
print(grocery_list)
 
print(grocery_list[1:4])
 
chritmas_presents = ['Car', 'Phone', 'iPad','Laptop']
things_to_buy = [chritmas_presents, grocery_list]
 
print(things_to_buy)
 
print(things_to_buy[1][1])
 
grocery_list.append('Salsa')
print(things_to_buy)
 
grocery_list.insert(100, "Tortia Chips")
print("Check", grocery_list)
 
grocery_list.remove("Tortia Chips")
 
grocery_list.sort()

grocery_list.reverse()
 
del grocery_list[4]
print(things_to_buy)
 
things_to_buy = chritmas_presents + grocery_list
print(things_to_buy)
 
print(len(things_to_buy))
 
print(max(things_to_buy))

print(min(things_to_buy))
 
int_tuple = (1,2,3,4,5)
 
list_tuple = list(int_tuple)
 
print(len(int_tuple))

print(max(int_tuple))

print(min(int_tuple))
 
super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
 
print(super_villains['Captain Cold'])
 
del super_villains['Fiddler']
print(super_villains)
 
super_villains['Pied Piper'] = 'Hartley Rathaway'
 
print(len(super_villains))

print(super_villains.get("Pied Piper"))
 
print(super_villains.keys())
 
print(super_villains.values())
 
age = 38
if age > 13 :
    print('You are a thanathini deanzas')
 
if age > 13 :
    print('You are a thanathini deanzas')
else :
    print('You are awesome')
 
if age >= 40 :
    print('You are a Kumrudheen')
elif age >= 35:
    print('You are a Deanzas')
else :
    print('You are an almost')
 
if ((age >= 13) and (age <= 45)):
    print("You are a Kumrudheen")
elif (age == 38) or (age >= 37):
    print("You are a Deanzas")
elif not(age == 38):
    print("You are a Kumrudheen")
else:
    print("You are still a Deanzas")
 
for x in range(0, 10):
    print(x , ' ', end="")

# /n is for newline 
print('\n')
 
grocery_list = ['Cookies', 'Cake', 'Strawberries', 'Bananas','Cheetos']
 
for y in grocery_list:
    print(y)
 
for x in [1,2,3,4,5]:
    print(x)
 
num_list =[[1,2,3],[10,20,30],[100,200,300]];
 
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
 
random_num = random.randrange(0,100)
 
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
 
