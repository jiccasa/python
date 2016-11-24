from os import system

def say(text):
	cmd="say " + text
	system(cmd)


# Main
Q_NAME = "Enter your first name and last name?"

say(Q_NAME)
name_inp=raw_input(Q_NAME)
fn,ln = name_inp.split(" ")
if (fn == Jessica or fn == Jiccasa):
	say("Hi"+fn)
	say("Hope you are doing fine")
	say("I admire you for your poem skills.")
	say("A good song lyrics from or you that I love the most")
	say("Ling Ling Ling")
	say("My name is Ling")
	say("Ling Ling Ling")
	say("And I can sing")
else:
	say("Hi"+fn)
	say("Hope you are doing fine")
	say("I admire you for your poem skills.")
