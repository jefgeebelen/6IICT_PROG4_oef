class Hond:
    naam = "Menno"
    massa = 65

    def blaf(self):
        print(f'{self.naam} zegt blaf.')

    def weegschaal(self):
        print(f'{self.naam} weegt {self.massa}.')

hond = Hond()
hond.blaf