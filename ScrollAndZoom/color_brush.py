from tkinter import *
from tkinter import colorchooser
import tkinter as tk

root = Tk()
#Function for choosing the color
def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    label = Label(root, text="You have chosen color {}".format(color[1])).pack(pady=10)
    #print(color)


colorchooser_button = Button(root, text='Select a color', command=choose_color).pack()
root.geometry("500x500")
root.mainloop()
