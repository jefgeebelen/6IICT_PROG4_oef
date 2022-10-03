""" Opdracht 3: (  /2)
1)
Vraag de gebruiker om een woord.
Maak OBV dit woord een dictionary:
 - keys: de letters in dit woord.
 - values: hoevaak iedere letter in dit woord voorkwam.

 >>> input: "hottentottententententoonstelling
     dict: {'h': 1, 'o': 4, 't': 10, 'e': 6, 'n': 7, 's': 1, 'l': 2, 'i': 1, 'g': 1}

2) sorteer de keys van de dictionary omgekeerd alfabetisch.
 >>> input: "hottentottententententoonstelling
     dict: {'t': 10, 's': 1, 'o': 4, 'n': 7, 'l': 2, 'i': 1, 'h': 1, 'g': 1, 'e': 6}
"""

"""oef1"""
dict = {}
woord = list(input("geef een woord"))
for leter in woord:
    if leter in dict:
        dict[leter] += 1
    else:
        dict[leter] = 1
print(dict)