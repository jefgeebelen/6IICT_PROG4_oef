import csv 

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" ) 

csv_reader = csv.DictReader( fp , delimiter=";")  
eruptions_ld = [] # ld = lijst van dictionaries 
eruptions_ld_verwert = []
for rij in csv_reader:
    print(rij) 
    eruptions_ld.append(rij)


fp.close() # Na sluiten is CSV niet meer bruikbaar 
print(eruptions_ld) 