""" Opdracht:
Bekijk machten.csv. In dit bestand zijn drie kolommen gegeven:
    - basis: Getallen van 1 tot en met 10.
    - kwadraat: Het kwadraat van de linksgelegen basisgetallen.
    - derdemacht: De derdemacht van de linksgelegen basisgetallen.
    OPGELET: dit bestand gebruikt komma als scheidingsteken, geen punt-komma.

Momenteel zijn enkel de kolommen basis en kwadraat ingevuld.
De opdracht is als volgt:
    1) Open machten.csv in Python. Print iedere rij van de bekomen tabel. 
    2) Vul de kolom derdemacht aan in deze tabel. 
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand. BVB. machten_verwerkt.csv.
OPGELET: Het verwerkte CSV-bestand moet komma's gebruiken als scheidingsteken. 

Puntenverdeling: (  / 5)
    1) Open en print machten.csv in Python (  / 1).
    2) Vul de kolom derdemacht aan in Python (  / 1).
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand (  / 1).
    4) Schrijf bij iedere regel code commentaar die uitlegt wat je doet ( / 1).
    5) De ingeleverde code bevat geen foutmeldingen (  / 1).
      OPGELET: Voor onderdelen 1, 2 en 3 kijk ik enkel naar code die NIET in commentaar staat.
"""

from audioop import add
import csv
from distutils.util import change_root 
fp = open( "C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/toetsscv/machten.csv", "r" ) 
data = [] # ld = lijst van dictionaries 
lijst2 = []
csv_reader = csv.reader( fp , delimiter=",")  
for rij in csv_reader:
    print(rij) 
    data.append(rij)

print(data) 

for index, lijst in enumerate(data):
    if index != 0:
        lijst[2] = int(lijst[0])*int(lijst[1])
        print(lijst)
fp2 = open( "C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/toetsscv/machten.csv", "w", newline="") 

csv_writer = csv.writer( fp , delimiter=";") 

csv_writer.writerow(data)
fp.close()
fp2.close() # Na sluiten is CSV niet meer bruikbaar 
 