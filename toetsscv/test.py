import csv 

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" ) 

csv_reader = csv.DictReader( fp , delimiter=";")  
eruptions_ld = [] # ld = lijst van dictionaries 
eruptions_ld_verwert = []
dict2 = {}
for rij in csv_reader: 
    print(rij)
    eruptions_ld.append(rij)


fp.close() # Na sluiten is CSV niet meer bruikbaar 

"""deel3/oef7"""

fp = open("eruptions_ll_verwerkt.csv", "w", newline="")

csv_writer = csv.DictWriter(fp , delimiter=";", fieldnames=["Year", "Name"])

csv_writer.writeheader()
for rij in eruptions_ll_verwert:
    csv_writer.writerow(rij)

fp.close()

