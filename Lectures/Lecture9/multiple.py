class Arbeidstaker:
    def __init__(self):
        self.penger = 0

    def get_paid(self, amount: int) -> None:
        self.penger += amount
    

class Student:
    def __init__(self):
        self.obliger = 0

    def lever_oblig(self) -> None:
        self.obliger += 1

#Det spiller en rolle om Student eller Arbeidstaker kommer først, siden 
# super() kallet vil gå på det første argumentet, hvis vi bruker super().__init__()
class Stipendiat(Student, Arbeidstaker):
    def __init__(self):
        #super().__init__()
        Arbeidstaker.__init__(self)
        Student.__init__(self)


if __name__ == "__main__":
    ola = Stipendiat()
    ola.lever_oblig()
    ola.get_paid(3000)

    print(f"Ola har {ola.penger} på konto og har levert {ola.obliger} obliger")