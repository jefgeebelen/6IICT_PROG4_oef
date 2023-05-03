# Vul aan op basis van de instructies in de OneNote.
class Bankrekening:
    def __init__(self, eigenaar, geld, leeftijd):
        self.eigenaar = eigenaar
        self.geld = geld
        self.leeftijd = leeftijd 
        self.bank = "KBC"
    
    def storten(self, bedrag, bericht):
        self.geld += bedrag
        print(f"{bedrag} euro toegevoegd. Reden: {bericht}")
    
    def afhalen(self, bedrag, bericht):
        if self.leeftijd < 16:
            print(f"{self.eigenaar} is te jong om geld af te halen.")
        else:
            self.geld -= bedrag
            print(f"{bedrag} euro afgehaald. Reden: {bericht}")

    def overzicht(self):
        print(f"{self.eigenaar} heeft {self.geld} euro staan bij {self.bank}")
    
    def overschrijven(self, bedrag, andere_rekening):
        if isinstance(andere_rekening, Bankrekening):
            self.geld -= bedrag
            andere_rekening.storten(bedrag, "") 
            print(f"{self.eigenaar} stort {bedrag} euro naar {andere_rekening} ")
        else:
            print("Geen geldige rekening meegegeven.")