from kortstokk import Kort, Kortstokk

def main():
    kortliste = []
    for _ in range(52):
        kortliste.append(Kort())
    kortstokk = Kortstokk(kortliste)
    
    print()
    print(f"Antall kort i stokken: {len(kortstokk)}")

    for _ in range(3):
        tilfeldig_kort = kortstokk.trekk()
        print()
        print(tilfeldig_kort)
        print(f"type: {type(tilfeldig_kort)}")
        print(f"Antall gjenværende kort: {len(kortstokk)}")



if __name__ == "__main__":
    main()

