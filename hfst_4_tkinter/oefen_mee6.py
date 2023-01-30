import tkinter as tk
import os
venster = tk.Tk()


# Functie maakt een label aan wanneer opgeroepen.
def nieuwe_knop():
    knop = tk.Button(master=venster, text="Klik ook op mij!")
    knop.pack()

# Knop aanmaken.
    # master: geef aan tot welke GUI de knop behoort.
    # text: boodschap van de knop.
    # command: aan welke functie is de knop gelinkt.
knop = tk.Button(master=venster, text="Klik op mij!", command=nieuwe_knop)

knop.pack()

venster.mainloop()
