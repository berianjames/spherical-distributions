from fisher import Fisher
from numpy import pi

a0 = pi/4
b0 = 0
x = Fisher(a = a0, b = b0)

print x.pdf(theta=a0,phi=b0)
print x.pdf(theta=pi - a0,phi=b0+pi)
