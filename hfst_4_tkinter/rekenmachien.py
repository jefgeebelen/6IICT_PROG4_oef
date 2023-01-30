import tkinter as tk

venster = tk.Tk()

venster.geometry("260x350")
veld = tk.Entry(master=venster, width=30, fg="black", bg="green")
veld.place(x=35, y=0)

def bereken(teken):
    veld.insert(1, teken)
    


knop1 = tk.Button(master=venster, command=bereken("1"), text="1", width=10, height=3)
knop1.place(x=5, y=20)
knop2 = tk.Button(master=venster, command=bereken("2"), text="2", width=10, height=3)
knop2.place(x=90, y=20)
knop3 = tk.Button(master=venster, command=bereken("3"), text="3", width=10, height=3)
knop3.place(x=175, y=20)
knop1 = tk.Button(master=venster, command=bereken("4"), text="4", width=10, height=3)
knop1.place(x=5, y=80)
knop2 = tk.Button(master=venster, command=bereken("5"), text="5", width=10, height=3)
knop2.place(x=90, y=80)
knop3 = tk.Button(master=venster, command=bereken("6"), text="6", width=10, height=3)
knop3.place(x=175, y=80)
knop1 = tk.Button(master=venster, command=bereken("7"), text="7", width=10, height=3)
knop1.place(x=5, y=140)
knop2 = tk.Button(master=venster, command=bereken("8"), text="8", width=10, height=3)
knop2.place(x=90, y=140)
knop3 = tk.Button(master=venster, command=bereken("9"), text="9", width=10, height=3)
knop3.place(x=175, y=140)
knop1 = tk.Button(master=venster, command=bereken("0"), text="0", width=10, height=3)
knop1.place(x=5, y=200)
knop2 = tk.Button(master=venster, command=bereken("+"), text="+", width=10, height=3)
knop2.place(x=90, y=200)
knop3 = tk.Button(master=venster, command=bereken("-"), text="-", width=10, height=3)
knop3.place(x=175, y=200)
knop1 = tk.Button(master=venster, command=bereken("="), text="=", width=10, height=3)
knop1.place(x=5, y=260)
knop2 = tk.Button(master=venster, command=bereken("CRL"), text="CRL", width=22, height=3)
knop2.place(x=90, y=260)

venster.mainloop()
