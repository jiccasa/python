#tkinter

from tkinter import *

def deanzas():
    print("No, you are a deanzas!!!")

tk=Tk()
btn=Button(tk,text="Am I a DelaCruz?",command=deanzas)
btn.pack()
