""" Niveau 1: los sommatie recursief op """
def sommatie(getal):
    if getal == 1:
        return 1
    vorige_sommatie = sommatie(getal-1)
    return getal + vorige_sommatie
print( sommatie(1) )   # 1
print( sommatie(2) )   # 3
print( sommatie(3) )   # 6
print( sommatie(4) )   # 10
print( sommatie(5) )   # 15
print( sommatie(100) ) # 5050


""" Niveau 2: los sommatie met while-loops op """
getal = 100
Sommatie = 1
while True:
    if getal == 1:
        break
    vorig_getal =  getal
    getal -= 1
    Sommatie += vorig_getal
print(Sommatie)