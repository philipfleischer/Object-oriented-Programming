def estimate_pi(n: int) -> float:
    """Estimerer pi med Leibniz formel (fra taylor-rekker)."""
    pi_delt_pa_4 = 0.0
    for i in range(n):
        pi_delt_pa_4 += (-1.0) ** i / (2.0 * i + 1.0)
    return 4 * pi_delt_pa_4
