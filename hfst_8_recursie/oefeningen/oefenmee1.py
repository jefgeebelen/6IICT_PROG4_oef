""" Vul aan in de OneNote """
def aftellen(getal):
    if getal < 1:
        return
    print(getal)
    aftellen(getal-1)
    print(getal)

aftellen(5)