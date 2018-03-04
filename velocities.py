import matplotlib
matplotlib.use('TkAgg')

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from parser.rd import RDRow
from parser.file import FileParser
from draw.galactic2cartesian import GalacticToCartesian
from utils import toHours, toDescending

from os.path import abspath, join, dirname
from numpy import sin, cos, arctan2, sqrt, abs, max, min, array, transpose
from math import pi
from numpy.linalg import lstsq



DATA_DIR = join(abspath('.'), 'data')

# Parsing data
rdrow = FileParser(RDRow)

datafile = join(DATA_DIR, 'III-239', 'catalog.dat')
print("Parsing datafile: {}".format(datafile))
rdrow.append(datafile)

print("Parsed {} objects".format(rdrow.row_number))

# Extract stars positions
right_ascencion = list(map(
    lambda rah: float(rah[0]) * pi / 12.,  # original h -> rad
    rdrow.get('rah')
))
declination = list(map(
    lambda ded: float(ded[0]) * pi / 180.,  # original deg -> rad
    rdrow.get('ded')
))

erah = list(map(
    lambda erah: float(erah[0]) * pi / 3600000. / 180.,  # original mas -> rad
    rdrow.get('erah')
))

eded = list(map(
    lambda eded: float(eded[0]) * pi / 3600000. / 180.,  # original mas -> rad
    rdrow.get('eded')
))


# Star proper motion RA/DEC
rv = list(map(lambda rv: float(rv[0]) * 1000., rdrow.get('rv')))  # original arcsec -> rad
erv = list(map(lambda erv: float(erv[0]) * 1000., rdrow.get('erv')))  # original arcsec -> rad

# Temporary values to simplify computations
sa, ca = sin(right_ascencion), cos(right_ascencion)
sd, cd = sin(declination), cos(declination)

A = []
b = []
ex = 0
ey = 0
ez = 0
for ridx in range(rdrow.row_number):
    A += [[cd[ridx] * ca[ridx], cd[ridx] * sa[ridx], sd[ridx]]]
    b += [[-rv[ridx]]]
    ex += (sd[ridx] * ca[ridx] * eded[ridx] + cd[ridx] * sa[ridx] * erah[ridx]) ** 2
    ey += (cd[ridx] * ca[ridx] * erah[ridx] - sd[ridx] * sa[ridx] * eded[ridx]) ** 2
    ez += (cd[ridx] * eded[ridx]) ** 2

((X, ), (Y, ), (Z, )), residual, rank, singular_values = lstsq(A, b, rcond=None)

mex = sqrt(ex)
mey = sqrt(ey)
mez = sqrt(ez)

A = arctan2(Y, X)
D = arctan2(Z, sqrt(X ** 2 + Y ** 2))

ea = arctan2(Y, X) / (1 + Y * Y / X / X) * (mex / Y - mey * X / Y / Y)
ed = arctan2(Y, sqrt(X * X + Y * Y)) * (sqrt(X ** 2 + Y ** 2) * mez - 2 * Z * X * mex - 2 * Z * Y * mey) / (X ** 2 + Y ** 2 + Z ** 2)

print('Solar apex is (RA) {0}h {1}m {2:2.3} +/- {5:2.3}s (dec) {6:2.4} +/- {8:2.4} {7}'.format(
    *toHours(A), *toHours(ea),
    *toDescending(D), *toDescending(ed)
))
print('Solar apex is (RA) 18h 03m 50.2s (dec) {:2.4}'.format(30 + 16.8 / 3600.))