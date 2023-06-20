class Boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.geleend_aan = ""

    def lenen(self, persoon):
        if self.geleend_aan != "":
            print(f"{self.titel} is reeds geleend aan {self.geleend_aan}.")
        else:
            self.geleend_aan = persoon
            print(f"{self.titel} geleend aan {self.geleend_aan}.")

    def inleveren(self):
        if self.geleend_aan != "":
            print(f"{self.geleend_aan} levert {self.titel} in.")
            self.geleend_aan = ""
        else:
            print(f"kan {self.titel} niet inleveren, het is niet geleend.")

    def uitleg(self):
        print(f"{self.titel} is geschreven door {self.auteur} in {self.jaar}.")
        if self.geleend_aan != "":
            print(f"{self.titel} is momenteel uitgeleend aan {self.geleend_aan}.")

class Bibliotheek:
    def __init__(self, naam):
        self.naam = naam
        self.boeken = []
        
    def toevoegen_boek(boek):

    def uitleg_boeken():

    def leen_boek(titel, persoon):

    def lever_boek_in(titel):










# """ Niveau 3: Leg in dit tekstveld uit waarom het aangegeven probleem optreed. 
#               Leg ook uit hoe je het kan oplossen.
#
#
#
# """