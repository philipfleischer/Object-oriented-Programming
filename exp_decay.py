class ExponentialDecay:
    """Representerer en difflikning (ODE) på formen:
    du/dt = -au"""
    
    def __init__(self, a: float):
        """a er decay-konstanten, kan ikke være negativ (da får mann
        ValueError)."""
        if a < 0:
            raise ValueError(f"ExponentialDecay.__init__: a er negativ ({a})")
        self._a = a


