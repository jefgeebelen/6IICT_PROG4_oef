# Import the Tkinter library
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
win = Tk()

# Define the geometry
win.geometry("750x350")

# Create Buttons in the frame
button = ttk.Button(win, text="Button-1")
button.place(x=1, y=1)

button = ttk.Button(win, text="Button-2")
button.place(x=325, y=175)

button = ttk.Button(win, text="Button-3")
button.place(x=325, y=225)

#Create a Label
Label(win, text="Position the Buttons", font='Consolas 15').pack()

win.mainloop()