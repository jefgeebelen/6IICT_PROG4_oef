import csv 

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r") 

csv_reader = csv.DictReader( fp , delimiter=";") 

eruptions_ld = [] # ld = lijst van dictionaries 
dict2 = {}
for rij in csv_reader: 
    eruptions_ld.append(rij)
    for index, dict in enumerate(eruptions_ld):
        for key, value in dict.items():
            del(eruptions_ld[index])
            if key != "":
                dict2[key] = value
            eruptions_ld.append(dict)
fp.close() # Na sluiten is CSV niet meer bruikbaar 
print(eruptions_ld) 
