""" Algemeen (gaat over oefening 1 en 2): (  / 2)
Schrijf bij iedere regel code commentaar (  / 1)
Zorg dat de code geen geeft foutmeldingen (  / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""

""" OEFENING 1: (  / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""

""" STAP 1: (  / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
import json #importeer de modulle json
fp = open("oefening1.json", "r") #open het bestand oefening1.json zodat je het kan lezen
dict = json.load(fp) #dict is gelijk aan de inhoud van fp(json bestand)
fp.close()  #sluit fp(het bestand)



""" STAP 2: (  / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""
print(f"{dict['voornaam']} is gebooren op {dict['geboortedatum']}. hij is de eigenaar van {dict['bedrijf']}. hiernaast speelt hij ook {dict['hobbys'][3]}.") #zin met info uit dictionary gehaalt.
""" STAP 3: (  / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""
verm_min = min(dict["vermogen_in_miljard"].values()) #verm_min is gelijk aan het minimum van dict vermogen_in_miljard in dict 
verm_max = max(dict["vermogen_in_miljard"].values()) #verm_max is gelijk aan het maximum van dict vermogen_in_miljard in dict 
fp = open("oefening1_DEEL2.json", "w")  #open/maak het bestand oefening1.json zo dat je er in kan schrijven
dict["verm_max"] = verm_max #key ver_max is gelijk aan de variabele verm_max
dict["verm_min"] = verm_min #key ver_max is gelijk aan de variabele verm_min
json.dump(dict, fp) #schrijf dict naar het bestand
fp.close() #sluit het bestand fp
""" STAP 4: (  / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""

