class Hond:
    def benoem(self, benaming):
        self.naam = benaming

    def wegen(self, massa):
        self.massa = massa

    def blaf(self):
        print(f"{self.naam} zegt blaf")

    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

dier = Hond()
dier.benoem("menno")
dier.blaf()
dier.wegen(3)
dier.weegschaal()