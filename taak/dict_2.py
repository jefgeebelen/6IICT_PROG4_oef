""" Opdracht 2:
Je krijgt een lijst van lijsten genaamd landen_steden.
1) Vorm deze om naar een dictionary van lijsten.
   De eerste lijst bevat alle keys. Deze moeten gekoppeld worden aan de overige lijsten.
   
   Te bekomen dictionary:
   {
    "USA":  ["Boston", "Pittsburgh", "Washington"],
    "UK":   ["London", "Edinburgh", "Belfast"],
    "Frankrijk": ["Parijs", "Lyon", "Avignon"],
    "Duitsland: ["Keulen", "Berlijn"]
   }

2) Vraag de gebruiker om een stad. 
   Gebruik de opgestelde dictionary om het land te printen waarin deze stad zich bevindt.
   >>> input: Lyon
       Frankrijk
"""
landen_steden = [
    ["USA", "UK", "Frankrijk", "Duitsland"],    # Landen
    ["Boston", "Pittsburgh", "Washington"],     # Steden USA
    ["London", "Edinburgh", "Belfast"],         # Steden UK
    ["Parijs", "Lyon", "Avignon"],              # Steden Frankrijk
    ["Keulen", "Berlijn"]                       # Steden Duitsland
]



dict_land = {}  #nieuwe lijst dict_land
for index, land in enumerate(landen_steden[0]):  #overloop iedere index in landen_steden[0] en overloop iedere waarde'(land) in landen_steden
    dict_land[land] = landen_steden[index+1]  #voeg aan de dictionary een key toe met de waarde van land en met als value een lijst van de lijsten landen_steden[]

print(dict_land) #print de dictionary dict_land

stad = input("Geef een stad: ") #vraag aan de gebruiker geef een stad en de waarde die ze geven assign aan stad 
for land, steden in dict_land.items(): #overloop iedere key(land) en iedere value(steden) in dict_land
    if stad in steden: #als stad in de lijst steden zit dan:
        print(land) #print land 
    else: #anders
        print("Stad niet in lijst.") #print stad niet in lijst
