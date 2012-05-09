def dcos(theta,phi):
    """Convert a set of position vectors of unit length
    (i.e. of unit length) to direction cosines."""
    from numpy import sin, cos
    
    x = sin(theta) * cos(phi)
    y = sin(theta) * sin(phi)
    z = cos(theta)

    return x, y, z

def pos(x,y,z):
    """Convert directional cosine (x,y,z) to position angle (theta,phi)."""
    from numpy import arccos, sin

    theta = arccos(z)
    phi = arccos(x / sin(theta))

    return theta, phi

def recenter(x,thetap,phip):
    """Find the coordinates of a set of position vectors
    relative to the pole (thetap, phip)."""
    
    return

class Fisher:
    """The two-parameter Fisher distribution."""

    def __init__(self, k=1, a=0, b=0):
        from numpy import pi, sinh

        self.k = k
        self.a = a
        self.b = b

        self.C = k / (4 * pi * sinh(k))

        return

    def pdf(self, theta=0, phi=0):
        """Compute pdf value at (theta,phi)"""
        from numpy import exp, sin, cos

        k = self.k
        a = self.a
        b = self.b

        pde = self.C * exp(k * (sin(theta) * sin(a) * cos(theta-b) + 
                                cos(theta) * cos(a)))

        return pde * sin(theta), pde

    def sample(self,n=1):
        """Sample n instances of a given Fisher distribution."""
        from numpy import exp, arcsin, sqrt, log, pi, array
        from numpy.random import rand
        
        k = self.k
        l = exp(-2 * k)

        R1 = rand(n)
        R2 = rand(n)

        T = 2 * arcsin( sqrt(-log(R1*(1-l)+l)/(2*k)) )
        P = 2 * pi* R2

        # Rotate T and P to desired mean
        #a = self.a
        #b = self.b
        #x, y, z = dcos(T, P)
        #A = array([[cos(a)*cos(b), cos(a)*sin(b), -sin(a)],
        #           [-sin(b), cos(b), 0],
        #           [sin(a)*cos(b), sin(a)*sin(b), cos(a)]])
        #px, py, pz = A.dot(array([x,y,z]).T)
        #theta, phi = pos(px, py, pz)

        return T, P#theta, phi
        
