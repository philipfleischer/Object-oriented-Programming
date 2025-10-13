from math import pi

class Kule:
    """Representerer en geometrisk kule i 3D."""
    def __init__(self, radius: float):
        self._radius = radius

    def __str__(self) -> str:
        return f"Kule med radius {self._radius}"
    
    @property
    def radius(self) -> float:
        """Runder av radius til 2 desimaler."""
        return round(self._radius, 2)
    
    @radius.setter
    def radius(self, ny_radius: int | float) -> None:
        """Gir ValueError hvis r er negativ.
        
        
        In Python, a "setter" is a method within a class used to set or modify the value 
        of an attribute. Setters are typically used in conjunction with "getters" (methods 
        to retrieve attribute values) to provide controlled access to an object's attributes, 
        promoting data encapsulation and allowing for validation or transformation of data before 
        it is assigned.
    While Python allows direct access to attributes, using setters (often implemented with the @property 
    decorator) offers advantages:
    Data Validation: Setters can include logic to validate the input value before assigning it to the 
    attribute, ensuring data integrity. For example, a setter for an age attribute might raise an error 
    if a negative value is provided.
    Encapsulation: Setters help encapsulate the internal representation of data, allowing you to change 
    the underlying implementation of an attribute without affecting how other parts of your code interact 
    with it.
    Controlled Access: Setters provide a specific point of control for modifying attribute values, enabling 
    you to add side effects or perform actions whenever an attribute is updated."""
        if ny_radius < 0: 
            raise ValueError(f"radius til Kule må være positiv: {ny_radius}")
        
        self._radius = float(ny_radius)
        self._areal = 4 * pi * ny_radius**2
        self._volum = (4/3) * pi * ny_radius**3


    @property
    def volum(self) -> float:
        """Runder av radius til 2 desimaler."""
        return round(self._volum, 2)
    
    @volum.setter
    def volum(self, nytt_volum: int | float) -> None:
        """Gir ValueError hvis nytt_volum er negtiv."""
        if nytt_volum < 0: raise ValueError(f"Volum må være positivt: {nytt_volum}")
        #Bruker radius() sin settter metode, for å unngå duplikat av kode
        self.radius = (3*nytt_volum / (4*pi))**(1/3)

    @property
    def areal(self) -> float:
        """Runder av areal til 2 desimaler."""
        return round(self._areal, 2)
    
    @areal.setter
    def areal(self, nytt_areal: int | float) -> None:
        """Gir ValueError hvis nytt_areal er negtiv."""
        if nytt_areal < 0: raise ValueError(f"areal må være positivt: {nytt_areal}")
        self.radius = (nytt_areal / (4*pi)**(1/2))
        

        


def main():
    ball = Kule(5)
    ball.radius += 5
    print(f"{ball} har volum {ball.volum}")
    try:
        negativ_kule = Kule(-1)
    except ValueError as e:
        print("Denne feilmeldingen er håndtert.", e)

    ball.volum = 523.6
    print()
    print(f"{ball} har volum {ball.volum}")

    ball._areal = 1256.64
    print()
    print(f"{ball} har volum {ball.volum}") 
    print(f"{ball} har areal {ball.areal}")



if __name__ == "__main__":
    main()
