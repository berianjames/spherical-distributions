from numpy import array, pi, sinh, sin, cos, exp

class Fisher:
    """The two-parameter Fisher distribution."""

    def __init__(self, k=1, a=0, b=0):
        self.k = k
        self.a = a
        self.b = b

        self.C = k / (4 * pi * sinh(k))

        return

    def pdf(self, theta=0, phi=0):
        """Compute pdf value at (theta,phi)"""

        k = self.k
        a = self.a
        b = self.b

        pde = self.C * exp(k * (sin(theta) * sin(a) * cos(theta-b) + 
                                cos(theta) * cos(a)))

        return pde * sin(theta), pde
        
        
