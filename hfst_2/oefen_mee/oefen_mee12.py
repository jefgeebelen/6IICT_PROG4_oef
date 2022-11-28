import json 
# Pad is afhankelijk van locatie appel.json 
fp = open("C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee12.json", "r") 
week = json.load(fp) 
fp.close()  # Na sluiten is JSON niet meer bruikbaar 
dagen = input('geef een dag:')
dag = week[dagen]
print("op maandag heb je volgende activiteiten gepland:") 
for index, activiteit in enumerate(dag):
    print(dag[index])
veranderen = input("Wil je deze activiteit wijzigen (j/n)?")
if veranderen == "j":
    fp = open("C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee12.json", "w") 
    verandering = input("Geef nieuwe activiteit(en) in:")
    x = verandering.split() 
    week[dagen] = x
    json.dump(week, fp)