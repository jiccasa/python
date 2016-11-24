import sys
import os
import random

# #Reversing strings

def reverse_string_1(str):
	rev_str = ""
	for chr in str:
		rev_str = chr + rev_str
	return rev_str


def reverse_string_2(str):
	return(str[::-1])

def reverse_string_3(str):
	return("".join(reversed(str)))


def reverse_sentence(sentence):
	s_list = sentence.split()
	rev_string = " ".join(str(element)for element in s_list[::-1])
	return (rev_string)





# #Main

s = "Jessica"
print(s)

print(reverse_string_1(s))
print(reverse_string_2(s))
print(reverse_string_3(s))





inp_sentence = input("Enter a sentence: ")

# Reverse the sentence
# Jessica Is A Deep Dish Deanzas   => saznaeD hsiD peeD A sI acisseJ
print(reverse_string_1(inp_sentence))


# Reverse the words in the sentense
# "She is god" = "god is She"

print(reverse_sentence(inp_sentence))
