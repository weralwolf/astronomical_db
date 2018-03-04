import matplotlib
matplotlib.use('TkAgg')

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from parser.ppm import PPMRow
from parser.file import FileParser
from draw.galactic2cartesian import GalacticToCartesian
from utils import toHours, toDescending

from os.path import abspath, join, dirname
from numpy import sin, cos, arctan2, sqrt, abs, max, min, array, transpose
from math import pi
from numpy.linalg import lstsq

DATA_DIR = join(abspath('.'), 'data')

# Parsing data
ppm = FileParser(PPMRow)

datafile_north = join(DATA_DIR, 'I_146', 'ppm1.dat')
print("Parsing north datafile: {}".format(datafile_north))
ppm.append(datafile_north)

datafile_south = join(DATA_DIR, 'I_193', 'ppm2.dat')
print("Parsing south datafile: {}".format(datafile_south))
ppm.append(datafile_south)

print("Parsed {} objects".format(ppm.row_number))

# Extract stars positions
right_ascencion = list(map(
    lambda hms: (int(hms[0]) + int(hms[1]) / 60. + float(hms[2]) / 3600.) * pi / 12.,  # original h -> rad
    ppm.get('rah', 'ram', 'ras')
))
declination = list(map(
    lambda sdms: (1 if sdms[0] == '+' else -1) * (int(sdms[1]) + int(sdms[2]) / 60. + float(sdms[3]) / 3600.) * pi / 180.,  # original deg -> rad
    ppm.get('de', 'ded', 'dem', 'des')
))
eras = list(map(
    lambda eras: float(eras[0]) * pi / 360000. / 180.,  # original 10mas -> rad
    ppm.get('eras')
))
edes = list(map(
    lambda edes: float(edes[0]) * pi / 360000. / 180.,  # original 10mas -> rad
    ppm.get('edes')
))

# Star proper motion RA/DEC
pm_ra = list(map(lambda pma: float(pma[0]) / 300. * pi, ppm.get('pmra')))  # original sec -> rad
pm_de = list(map(lambda pmd: float(pmd[0]) / 20. * pi, ppm.get('pmde')))  # original arcsec -> rad

# Temporary values to simplify computations
sa, ca = sin(right_ascencion), cos(right_ascencion)
sd, cd = sin(declination), cos(declination)

A = []
b = []
ex = 0
ey = 0
ez = 0
k = 4.74
for ridx in range(ppm.row_number):
    A += [
        [sa[ridx], -ca[ridx], 0],
        [sd[ridx] * ca[ridx], sd[ridx] * sa[ridx], -cd[ridx]]
    ]
    ex += (ca[ridx] * eras[ridx])**2 + (cd[ridx] * edes[ridx])**2
    ey += (sa[ridx] * eras[ridx])**2 + (cd[ridx] * sa[ridx] * edes[ridx] + sd[ridx] * ca[ridx] * eras[ridx])**2
    ez += (sd[ridx] * edes[ridx])**2
    b += [
        [k * pm_ra[ridx] * cd[ridx]],
        [k * pm_de[ridx]]
    ]

result, residual, rank, singular_values = lstsq(A, b, rcond=None)
(X, ), (Y, ), (Z, ) = result

mex = sqrt(ex)
mey = sqrt(ey)
mez = sqrt(ez)

A = arctan2(Y, X)
D = arctan2(Z, sqrt(X * X + Y * Y))

ea = arctan2(Y, X) / (1 + Y * Y / X / X) * (mex / Y - mey * X / Y / Y)
ed = arctan2(Y, sqrt(X * X + Y * Y)) * (sqrt(X ** 2 + Y ** 2) * mez - 2 * Z * X * mex - 2 * Z * Y * mey) / (X ** 2 + Y ** 2 + Z ** 2)

if A < 0:
    A += 2 * pi

Ah = int(A * 12 / pi)
Am = int(A * 12 * 60 / pi - Ah * 60)
As = A * 12 * 3600 / pi - Ah * 3600 - Am * 60

Dd = int(abs(D * 180. / pi))
Ds = 'N' if D > 0 else 'S'

print('Solar apex is (RA) {0}h {1}m {2:2.3} +/- {5:2.3}s (dec) {6:2.4} +/- {8:2.4} {7}'.format(
    *toHours(A), *toHours(ea),
    *toDescending(D), *toDescending(ed)
))
print('Solar apex is (RA) 18h 03m 50.2s (dec) {:2.4}'.format(30 + 16.8 / 3600.))
