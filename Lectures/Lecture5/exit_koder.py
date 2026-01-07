import sys

def main(argumenter: list[str]) -> int:
    """Antar at argumenter er to tall, deler det første på det siste."""
    if len(argumenter) != 2:
        print("Trenger nøyaktig 2 arguemnter")
        return 2 # exit-kode
    else:
        print(f"Resultatet er {float(argumenter[0]) / float(argumenter[1])}")
        #return None

if __name__=="__main__":
    # exit(2) tilsvarer exit code 2
    # exit(None) tilsvarer exit code 0 = alt gikk bra
    exit(main(sys.argv[1:]))