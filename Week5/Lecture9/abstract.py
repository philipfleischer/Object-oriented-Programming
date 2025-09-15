#Abstract Base Class
from abc import ABC, abstractmethod

#Why do we do this?
class Swimming(ABC):
    @abstractmethod
    def swim(self) -> None:
        raise NotImplementedError("Swim() must be implemented")
    

class Flying(ABC):
    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError("fly() must be implemented.")
    

#Arver fra begge de abstrakte klassene
class Duck(Swimming, Flying):
    def swim(self) -> None:
        print("The duck is swimming.")

    def fly(self) -> None:
        print("The duck is flying.")


class Penguin(Swimming):
    def swim(self) -> None:
        print("The penguin is swimming,")


if __name__ == "__main__":
    #testObject = Swimming()
    #testObject.swim()

    objects: list[object] = [Duck(), "not a bird", Penguin()]

    for obj in objects:
        # isinstance sjekker om objektet er av type Flying
        # ELLER noe som arver fra Flying (samme for Swimming under)
        if isinstance(obj, Flying):  obj.fly()
        if isinstance(obj, Swimming): obj.swim()