class Duck:
    """"""

    def swim(self) -> None:
        print("The duck is swimming.")

    def fly(self) -> None:
        print("The duck is flying.")

    
class Goose:
    def swim(self) -> None:
        print("The goose is swimming.")

    def fly(self) -> None:
        print("The goose is flying.")


class Swan:
    def swim(self) -> None:
        print("The Swan is swimming.")

    def fly(self) -> None:
        print("The Swan is flying.")


if __name__ == "__main__":
    ducks: list[Duck] = [Duck(), Goose(), Swan()]

    for duck in ducks:
        duck.fly()
        duck.swim()