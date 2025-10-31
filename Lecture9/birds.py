class Bird:
    def swim(self) -> None:
        print(f"The {type(self).__name__.lower()} is swimming.")

    def fly(self) -> None:
        print(f"The {type(self).__name__.lower()} is flying.")

class Duck(Bird):
    pass

class Goose(Bird):
    pass

class Swan(Bird):
    pass


if __name__ == "__main__":
    birds: list[Bird] = [Duck(), Goose(), Swan()]

    for bird in birds:
        bird.fly()
        bird.swim()