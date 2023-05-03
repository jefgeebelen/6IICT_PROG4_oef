class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

honden = Hond("Floris", 8)
honden.weegschaal()

honden = Hond("Fido", 3)
honden.weegschaal()
