import tkinter as tk

venster = tk.Tk()

# Knop aanmaken.
    # master: geef aan tot welke GUI de knop behoort.
    # text: boodschap van de knop.
knop = tk.Button(master=venster, text="Klik op mij!")

knop.pack()

venster.mainloop()