#OOP-Live coding
from random import shuffle

class Kort:
    """Representerer et kort av en elelr annen type."""
    pass

class Kortstokk:
    """Representerer en kortstokk med kort av en eller annen type."""
    
    def __init__(self, kortene: list[Kort] = []):
        """Lager en kortstokk. Tom hvis uten argument, ellers inneholder 
        den kortene i listen."""
        self._kortene = kortene

    def stokk(self) -> None:
        """Stokker kortene i tilfeldig rekkefølge."""
        shuffle(self._kortene)
    
    def trekk(self) -> Kort:
        """returnerer og fjerner det øverste (siste) kortet fra kortstokken (stack)"""
        #trukket_kort = self._kortene[-1]
        #del self._kortene[-1]
        #Bedre måte å gjøre det på, returnerer og fjerener siste element:
        trukket_kort = self._kortene.pop()
        return trukket_kort

    #MAgisk metode som gir oss lengden på en datastruktur eller objekt
    def __len__(self) -> int:
        return len(self._kortene)
    
    




