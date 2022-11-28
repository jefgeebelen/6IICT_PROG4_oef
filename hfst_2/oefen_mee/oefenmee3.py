import csv 
import pandas as pd
 
fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r", ignore_index=True) 

csv_reader = csv.DictReader( fp , delimiter=";") 

eruptions_ld = [] # ld = lijst van dictionaries 

for rij in csv_reader: 

    print(rij) 

    eruptions_ld.append(rij) 

 

fp.close() # Na sluiten is CSV niet meer bruikbaar 

 

print("") 

print(eruptions_ld) 