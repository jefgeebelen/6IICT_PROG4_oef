""" Opdracht 3: (  /3)
1) Vorm ranglijst_eten om naar een dictionary (zie voorbeeld). (  /2)

2) Dezelfde code moet ook werken voor andere ranglijsten, (  /1)
   zowel wanneer deze meer als minder rangen nodig hebben.
   Het maximum aantal rangen die een lijst kan hebben is 7.
   De rangen zijn A, B, C, D, E, F, G.

De totaalscore van deze toets is 10. Alle opdrachten zijn samen 9 punten waard.
Het laatste punt staat op het schrijven van code zonder foutmeldingen.
"""

ranglijst_eten = [
    ["water"],                                  # A
    ["groenten", "fruit", "soja", "granen"],    # B
    ["vis", "gevolgte", "kaas", "zuivel"],      # C
    ["rood vlees", "boter"],                    # D
    ["snoep", "zout", "alcohol", "fast food"]   # E
]

""" Te bekomen dictionary voor ranglijst_eten: 
{
    "A": ["water"],
    "B": ["groenten", "fruit", "soja", "granen"],
    "C": ["vis", "gevolgte", "kaas", "zuivel"],
    "D": ["rood vlees", "boter"], 
    "E": ["snoep", "zout", "alcohol", "fast food"]
}
"""

ranglijst_eten_2 = [
    ["water"],                                  # A
    ["groenten", "fruit", "soja", "granen"],    # B
    ["vis", "gevolgte", "kaas", "zuivel"],      # C
    ["rood vlees", "boter"],                    # D
    ["zout", "alcohol"],                        # E
    ["snoep", "fast food"],                     # F
    ["potgrond", "houtschors", "mos"],          # G
]

""" Te bekomen dictionary voor ranglijst_eten_2: 
{
    "A": ["water"],
    "B": ["groenten", "fruit", "soja", "granen"],
    "C": ["vis", "gevolgte", "kaas", "zuivel"],
    "D": ["rood vlees", "boter"], 
    "E": ["zout", "alcohol"],
    "F": ["snoep", "fast food"],
    "G": ["potgrond", "houtschors", "mos"],
}
"""
dict_ranglijst_eten = {}
rang = ["A", "B", "C", "D", "E", "F", "G", ]
for index, list in enumerate(ranglijst_eten):
    dict_ranglijst_eten[rang[index]] = list
print(dict_ranglijst_eten)
