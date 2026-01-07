class LazyProgrammerError(Exception):
    pass


# \ betyr å fortsette på neste linje
def vektor_addisjon(u: list[int | float], 
                    v: list[int | float]) \
                    -> list[int | float]:
        """Tolker to lister som 3D-vektorer og adderer dem elementvis."""
        w = []
        n = max(len(u), len(v))
        for i in range(n):
            try:
                #Antar lik lengde (litt naivt)
                w.append(u[i] + v[i])
            except IndexError:
                #Antar v er for kort, bruker 0 som v-verdi
                try:
                    w.append(u[i] + 0)
                except IndexError:
                    #Antar u er for kort, bruker 0 som u-verdi
                    w.append(0 + v[i])
                except NotImplementedError:
                    print("Not implemented yet")
                    raise LazyProgrammerError("Have you forgetten to implement code?")
        return w

