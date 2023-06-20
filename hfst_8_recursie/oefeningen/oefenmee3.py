""" Bepaal de faculteit van een getal met behulp van een while-loop. """
getal = 9
facaliteit = 1
while True:
    if getal == 1:
        break
    vorig_getal =  getal
    getal -= 1
    facaliteit *= vorig_getal
print(facaliteit)