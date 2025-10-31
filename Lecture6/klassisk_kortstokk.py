from kortstokk import Kort

#Lager en klase klassiskKort som arver fra klassen Kort
class KlassiskKort(Kort):
    @staticmethod
    def lovlige_symboler() -> list[str]:
        """Alle de 4 klassiske symbolene på spillkort uten joker."""
        return ["hjerter", "kløver", "ruter", "spar"]

    """Representerer et klasisk spillkort"""
    def __init__(self, symbol: str, verdi: int):
        """symbol = hjerter, kløver, ruter eller spar."""
        """verdi = tallverdi eller j = 11, Q = 12, K = 13 (1 teller som A)."""
        symbol = symbol.lower() # endre til små bokstaver, for å redusere feil
        if symbol not in KlassiskKort.lovlige_symboler():
            raise ValueError(symbol + " er ikke en type klasisk spillkort")
        self.symbol = symbol

        if self.symbol in ["herter", "ruter"]:
            self.farge = "rød"
        else:
            self.farge = "svart"
        
        if (verdi < 1) or (verdi > 13):
            raise ValueError(verdi + " er en ugyldig verdi for klassisk spillkort\n")
        self.verdi = verdi

    def tekst(self) -> str:
        """Returnerer teksten på kortet (tall / bokstav)."""
        if self.verdi == 1:
            return "A"
        elif self.verdi < 11:
            return str(self.verdi)
        else: #self.verdi >= 11
            return ["J", "Q", "K"][self.verdi - 11]

    def __str__(self) -> str:
        """Skriver ut hvilket kort dette er."""
        return self.symbol + " " + self.tekst()

class KlassiskKortstokk(Kortstokk):
    """REpresenterer en kortstokk med klassiske spillkort."""

    def __init__(self):
        """Lager alle 52 spillkort uten å stokke dem."""
        kortliste = []
        for symbol in KlassiskKort.lovlige_symboler():
            for i in range(1, 14):
                kort = klassiskKort(symbol, i)
                kortliste.append(kort)
        #Kaller moderklassen sin INIT metode istedet for å skrive det samme på nytt
        super()._init__(kortliste)


"""def main():
    kort = Kort()
    klassiskKortstokk = KlassiskKort(kort)
    print(klassiskKortstokk("J", 2))



if __name__ == "__main__":
    main()"""

