from numpy import abs
from math import pi


def toHours(A):
    if A < 0:
        A += 2 * pi

    Ah = int(A * 12 / pi)
    Am = int(A * 12 * 60 / pi - Ah * 60)
    As = A * 12 * 3600 / pi - Ah * 3600 - Am * 60
    return Ah, Am, As


def toDescending(D):
    return float(abs(D * 180. / pi)), 'N' if D > 0 else 'S'