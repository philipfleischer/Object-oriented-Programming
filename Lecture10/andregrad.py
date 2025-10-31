class AndregrasPolynom:
    """Klasse som representerer et andregradspolynom: a*x**2 + b*x + c"""
    def __init__(self, 
                 a: float | int=1, 
                 b: float |int=0, 
                 c: float | int=0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        """Runder av koeffesientene til 2 desimaler"""
        return f"AndregradsPolynom( a = {round(self.a, 2)}, " \
                                    + f"b = {round(self.b, 2)}, " \
                                    + f"c = {round(self.c, 2)} )"
    
if __name__ == "__main__":
    test = AndregrasPolynom()
    print(test)

    test.b = 1
    test.c = -1
    print(test)