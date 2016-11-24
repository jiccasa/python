from os import system

def say(text):
	cmd="say " + text
	system(cmd)

equation = input("Please enter an equation in this format - a + b: ")

el = equation.split()
num1,opr,num2 = int(el[0]), el[1], int(el[2])

if opr == '+':
    print("%d %s %d = %f" % (num1, opr, num2, num1 + num2))

elif opr == '-':
    print("%d %s %d = %f" % (num1, opr, num2, num1 - num2))

elif opr == '*':
    print("%d %s %d = %f" % (num1, opr, num2, num1 * num2))

elif opr == '/':
    print("%d %s %d = %f" % (num1, opr, num2, num1 / num2))

elif opr == '%':
    print("%d %s %d = %f" % (num1, opr, num2, num1 % num2))

else:
    print("You are a Deanzas. Give a proper equation")
    say("You are a Deanzas. Give a proper equation")




