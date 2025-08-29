# \ betyr å fortsette på neste linje
def vektor_addisjon(u: list[int | float], 
                    v: list[int | float]) \
                    -> list[int | float]:
        """Tolker to lister som 3D-vektorer og adderer dem elementvis."""
        w = []
        n = max(len(u), len(v))
        for i in range(n):
            w.append(u[i] + v[i])
        return w
