import json 
# Pad is afhankelijk van locatie appel.json 
fp = open("C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee8.json", "r") 
week = json.load(fp) 
fp.close()  # Na sluiten is JSON niet meer bruikbaar 
daggen = input('geef een dag:')
dag = week[daggen]
print("op maandag heb je volgende activiteiten gepland:") 
for index, activiteit in enumerate(dag):
    print(dag[index])
