from collections import OrderedDict

from .row import RowParser


class RDRow(RowParser):
    seed = [
        OrderedDict([
            ('rah', (0, 12)),  #   1- 12  F12.9  h      RAhour  Right Ascension J2000.0, epoch 1991.25
            ('ded', (13, 25)),  #  14- 25  F12.8 deg     DEdeg   Declination J2000.0, epoch 1991.25
            ('erah', (25, 31)),  #  26- 31  F6.1  mas   e_RAhour  Standard error in RA*cos(DEdeg)
            ('eded', (31, 37)),  #  32- 37  F6.1  mas   e_DEdeg   Standard error in DEdeg
            ('plx', (37, 45)),  #  38- 45  F8.2  mas     Plx     ?=9999.99 Trigonometric parallax
            ('eplx', (45, 52)),  #  46- 52  F7.2  mas   e_Plx     ?=999.99 Standard error in Plx
            ('pmra', (52, 61)),  #  53- 61  F9.2  mas/yr  pmRA    Proper Motion in RA*cos(DEdeg)
            ('pmde', (61, 70)),  #  62- 70  F9.2  mas/yr  pmDE    Proper Motion in DE
            ('epmra', (70, 77)),  #  71- 77  F7.2  mas/yr  e_pmRA  Standard error in pmRA
            ('epmde', (77, 84)),  #  78- 84  F7.2  mas/yr  e_pmDE  Standard error in pmDE
            ('bmag', (84, 91)),  #  85- 91  F7.3  mag     Bmag    ?=99.999 B magnitude in Johnson system
            ('vmag', (91, 98)),  #  92- 98  F7.3  mag     Vmag    ?=99.999 V magnitude in Johnson system
            ('ebmag', (98, 104)),  #  99-104  F6.3  mag   e_Bmag    ?=9.999 Standard error on B magnitude
            ('evmag', (104, 110)),  # 105-110  F6.3  mag   e_Vmag    ?=9.999 Standard error on V magnitude
            ('scat', (110, 116)),  # 111-116  F6.3  mag     Scat    ?=9.999 Scatter on magnitude
            ('v1', (117, 118)),  #     118  A1    ---     v1     *[GN ] Known variability from GCVS/NSV
            ('v2', (118, 119)),  #     119  A1    ---     v2     *[UVW ] Variability from Tycho-1
            ('v3', (119, 120)),  #     120  A1    ---     v3     *[CDMPRU ] Variability type
            ('v4', (120, 121)),  #     121  A1    ---     v4     *[VYIXR ] Variability from CMC11
            ('d12', (121, 123)),  # 122-123  A2    ---     d12    *[A-S ] CCDM component identifier (Cat. I/274)
            ('d3', (123, 124)),  #     124  A1    ---     d3     *[A-S ] Component identifier
            ('d4', (124, 125)),  #     125  A1    ---     d4     *[DRSYZ ] Duplicity from Tycho-1
            ('d5', (125, 126)),  #     126  A1    ---     d5     *[CGOVX ] Double/Multiple Systems flag
            ('d6', (126, 127)),  #     127  A1    ---     d6      [D ] Duplicity flag from PPM
            ('sptype', (128, 140)),  # 129-140  A12   ---     SpType  MK Spectral type (from ASCC-2.5)
            ('hip', (141, 147)),  # 142-147  I6    ---     HIP     ?=0 Hipparcos number (Cat. I/239)
            ('hd', (148, 154)),  # 149-154  I6    ---     HD      ?=0 HD number (Cat. III/135)
            ('ascc', (155, 162)),  # 156-162  I7    ---     ASCC    ASCC-2.5 (Cat. I/280) number
            ('gcrv', (163, 168)),  # 164-168  I5    ---     GCRV    GCRV (Cat. III/213) number
            ('ccdm', (169, 182)),  # 170-182  A13   ---     CCDM   *CCDM number of multiple star and its components
            ('mag', (183, 188)),  # 184-188  F5.2  mag     mag     ?=99.99 Visual or photographic GCRV magnitude
            ('nmag', (189, 190)),  #     190  A1    ---   n_mag    *[* ] indicates a photographic mag
            ('umag', (190, 191)),  #     191  A1    ---   u_mag    *[V: ] variability or uncertainty on mag
            ('spgcrv', (192, 203)),  # 193-203  A11   ---     SpGCRV  ? MK Spectral type from GCRV (Cat. III/213)
            ('rv', (204, 211)),  # 205-211  F7.2  km/s    RV      Average Radial Velocity
            ('erv', (211, 216)),  # 212-216  F5.1  km/s  e_RV      ?=-9.9 Mean standard error in RV
            ('nrv', (217, 218)),  #     218  A1    ---   n_RV     *[Gge ] Note on RV
            ('urv', (218, 219)),  #     219  A1    ---   u_RV     *[:* ]
            ('qrv', (219, 220)),  #     220  A1    ---   q_RV     *[A-E I] Quality index of the RV
            ('frv', (220, 221)),  #     221  A1    ---   f_RV     *[SOCR ] Flag of star type
            ('orv', (221, 225)),  # 222-225  I4    ---   o_RV      ?=0 Number of observations
            ('nmult', (225, 227)),  # 226-227  I2    ---   N_mult    [1,2] Number of matches for given GCRV entry
        ])
    ]
    drop_lines = 0