# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: vertaal input van gebruiker naar het Engels
kleuren_dict = {"rood":"red","groen":"green","blauw":"blue"}
# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def text():
    global kleur
    label = tk.Label(master=venster, text=f"mijn favoriete kleur is {kleur}", height=2, fg=kleuren_dict[kleur])
    label.pack()
knop = tk.Button(master=venster, text="Klik op mij!", command=text)
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()