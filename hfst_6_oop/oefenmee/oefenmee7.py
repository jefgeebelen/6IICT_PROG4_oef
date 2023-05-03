class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")
    
    def wijzig_naam(self, hernoem):
        print(f"{self.naam} heet nu {hernoem}")
        self.naam = hernoem

    def eten(self, hoeveelheid):
        self.massa += hoeveelheid*0.6
        print(f"{self.naam} weegt nu {self.massa}")

honden = Hond("Lucky", 5)
honden.weegschaal()
honden.wijzig_naam("bolly")
honden.eten(0.7)